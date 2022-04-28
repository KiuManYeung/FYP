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
global execution_sequence''')

        self.graphs = insert = ast.parse('''
mySpecialGraph = callsviz(varnames=[''' + "'" + self.vars + "'" + '''])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, "png", str(png_counter).zfill(4)))
''')
        self.processed = self.original

        self.do_global = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)
        self.do_before = (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef, ast.Return, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith, ast.Try, ast.Import, ast.ImportFrom, ast.Global, ast.Nonlocal, ast.Pass, ast.Break, ast.Continue)
        self.do_start_with = (ast.FunctionDef, ast.AsyncFunctionDef, ast.For, ast.AsyncFor, ast.While, ast.With, ast.AsyncWith, ast.If)

        self.insert_graphs(self.processed)
        self.insert_global(self.processed)
        self.insert_imports(self.processed)

    def lineno_builder(self, lineno, graph):
        insert = ast.parse('''execution_sequence.append(('''+ str(lineno) +''','''+ str(graph) +'''))''')
        return insert
        
    def clean_lineno(self, node, lineno):
        if hasattr(node, 'lineno'):
            node.lineno = lineno
        if hasattr(node, 'body'):
            for element in node.body:
                self.clean_lineno(element, lineno)

    def insert_graphs(self, node):
        if hasattr(node, 'body'):
            if isinstance(node, (ast.Try, ast.If)):
                for element in node.orelse:
                    self.insert_graphs(element)  
                temp = []
                if node.orelse:
                    temp = temp + self.lineno_builder(node.orelse[0].lineno-1, 1).body
                    self.clean_lineno(self.graphs, node.lineno)
                    temp = temp + self.graphs.body
                for element in node.orelse:
                    if isinstance(element, self.do_before):
                        temp = temp + self.lineno_builder(element.lineno, 0).body
                        temp.append(element)
                    elif isinstance(element, self.do_start_with):
                        temp.append(element)
                    else:
                        temp = temp + self.lineno_builder(element.lineno, 1).body
                        temp.append(element)
                        self.clean_lineno(self.graphs, element.lineno)
                        temp = temp + self.graphs.body
                node.orelse = temp
            if isinstance(node, ast.Try):
                for element in node.finalbody:
                    self.insert_graphs(element)  
                temp = []
                if node.finalbody:
                    temp = temp + self.lineno_builder(node.finalbody[0].lineno-1, 1).body
                    self.clean_lineno(self.graphs, node.lineno)
                    temp = temp + self.graphs.body
                for element in node.finalbody:
                    if isinstance(element, self.do_before):
                        temp = temp + self.lineno_builder(element.lineno, 0).body
                        temp.append(element)
                    elif isinstance(element, self.do_start_with):
                        temp.append(element)
                    else:
                        temp = temp + self.lineno_builder(element.lineno, 1).body
                        temp.append(element)
                        self.clean_lineno(self.graphs, element.lineno)
                        temp = temp + self.graphs.body
                node.finalbody = temp

            for element in node.body:
                self.insert_graphs(element)
            temp = []
            if isinstance(node, self.do_global) :
                temp = temp + self.globals.body
            if isinstance(node, self.do_start_with):
                temp = temp + self.lineno_builder(node.lineno, 1).body
                self.clean_lineno(self.graphs, node.lineno)
                temp = temp + self.graphs.body
            for element in node.body:
                if isinstance(element, self.do_before):
                    temp = temp + self.lineno_builder(element.lineno, 0).body
                    temp.append(element)
                elif isinstance(element, self.do_start_with):
                    temp.append(element)
                else:
                    temp = temp + self.lineno_builder(element.lineno, 1).body
                    temp.append(element)
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
global execution_sequence
execution_sequence = []''')
        i = 0
        for i in range(len(node.body)):
            if not isinstance(node.body[i], (ast.Import, ast.ImportFrom)):
                break
        node.body = node.body[0:i] + global_variables.body + node.body[i:]




# img_path = os.path.join(os.path.curdir, "png")
# if os.path.isdir(img_path):
#     shutil.rmtree(img_path)
# os.mkdir(img_path)
with open("fibo.py", 'r') as file:
    text = file.read()

namespace = {}
src = Handler(text)
with open("out.py", 'w') as out:
    out.write(ast.unparse(src.processed))
    # out.write(pformat(src.original, show_offsets=False))
exec(compile(src.processed, filename="<src>", mode="exec"), namespace)
print(namespace['execution_sequence'])
print(len(namespace['execution_sequence']))