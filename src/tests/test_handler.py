import ast
import os
import shutil
import traceback
from astpretty import pformat

class Handler:
    def __init__(self, original):

        self.error_msg = ""
        try:
            self.original = ast.parse(original)
        except Exception as e:
            # Probably only catches syntax errors
            self.error_msg = traceback.format_exc()
            self.original = ast.parse("")

        self.imports = ast.parse('''
from lolviz import *
import os
''')
        self.clean_lineno(self.imports, -1)

        self.vars = "','".join(list({node.id for node in ast.walk(self.original) if isinstance(node, ast.Name)}))
        
        self.globals = ast.parse('''
global png_counter
global graph_lines''')

        self.graphs = insert = ast.parse('''
mySpecialGraph = callsviz(varnames=[''' + "'" + self.vars + "'" + '''])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, "png", str(png_counter).zfill(4)))
''')
        self.processed = self.original

        self.do_global = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        self.do_not_follow = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Return, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith, ast.Try, ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal, ast.Pass, ast.Break, ast.Continue)

        
        self.insert_graphs(self.processed)
        self.insert_global(self.processed)
        self.insert_imports(self.processed)

    def lineno_builder(self, line_numbers):
        insert = ast.parse('''print("Executing line: '''+ str(line_numbers) +'''")''')
        return insert
        
    def clean_lineno(self, node, lineno):
        if hasattr(node, 'lineno'):
            node.lineno = lineno
        if hasattr(node, 'body'):
            for element in node.body:
                self.clean_lineno(element, lineno)

    def insert_graphs(self, node):
        if hasattr(node, 'body'):
            if isinstance(node, ast.Try):
                for element in node.orelse:
                    self.insert_graphs(element)  
                temp = []
                for element in node.orelse:
                    temp.append(element)
                    if not isinstance(element, self.do_not_follow):
                        self.clean_lineno(self.graphs, element.lineno)
                        temp = temp + self.graphs.body
                node.orelse = temp

                for element in node.finalbody:
                    self.insert_graphs(element)  
                temp = []
                for element in node.finalbody:
                    temp.append(element)
                    if not isinstance(element, self.do_not_follow):
                        self.clean_lineno(self.graphs, element.lineno)
                        temp = temp + self.graphs.body
                node.finalbody = temp

            for element in node.body:
                self.insert_graphs(element)
            temp = []
            if isinstance(node, self.do_global) :
                temp = temp + self.globals.body
            for element in node.body:
                temp.append(element)
                if not isinstance(element, self.do_not_follow):
                    self.clean_lineno(self.graphs, element.lineno)
                    temp = temp + self.graphs.body
            # if isinstance(node, ast.Module):
            #     temp = temp[:-4]
            node.body = temp

    def insert_imports(self, node):
        node.body = self.imports.body + node.body

    def insert_global(self, node):
        global_variables = ast.parse('''global png_counter
png_counter = 0
global graph_lines
graph_lines = []''')
        i = 0
        for i in range(len(node.body)):
            if not isinstance(node.body[i], (ast.Import, ast.ImportFrom)):
                break
        node.body = node.body[0:i] + global_variables.body + node.body[i:]


with open("bstree.py", 'r') as source:
    text = source.read()



# img_path = os.path.join(os.path.curdir, "png")
# if os.path.isdir(img_path):
#     shutil.rmtree(img_path)
# os.mkdir(img_path)
namespace = {}
src = Handler(text)
with open("out.py", 'w') as out:
    out.write(ast.unparse(src.processed))
    # out.write(pformat(src.original, show_offsets=False))
# exec(compile(src.processed, filename="<src>", mode="exec"), namespace)
