import ast
import os
import shutil
import traceback

class Handler:
    def __init__(self, original):
        try:
            self.original = ast.parse(original)
        except Exception as e:
            # print(e)
            msg = traceback.format_exc()
            self.original = ast.parse("")
        

        self.imports = ast.parse('''
from lolviz import *
import os
''')
        self.clean_lineno(self.imports, -1)

        self.vars = "','".join(list({node.id for node in ast.walk(self.original) if isinstance(node, ast.Name)}))
        
        self.global_count = ast.parse('''
global png_counter
global graph_lines''')

        self.graphs = insert = ast.parse('''
mySpecialGraph = callsviz(varnames=[''' + "'" + self.vars + "'" + '''])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, "png", str(png_counter).zfill(4)))
''')
        self.processed = self.original

        self.insert_imports(self.processed)
        self.insert_graphs(self.processed)
        self.insert_global(self.processed)

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
            for element in node.body:
                self.insert_graphs(element)
            temp = []
            if isinstance(node, ast.FunctionDef) :
                temp = temp + self.global_count.body
            for element in node.body:
                # if not isinstance(node, (ast.Import, ast.ImportFrom, ast.ClassDef)):
                    # temp = temp + self.lineno_builder(element.lineno).body
                # temp.append(element)
                if not isinstance(element, (ast.Import, ast.ImportFrom, ast.ClassDef, ast.FunctionDef, ast.Return)):
                    # temp = temp + self.lineno_builder(element.lineno).body
                    temp.append(element)
                    self.clean_lineno(self.graphs, element.lineno)
                    temp = temp + self.graphs.body
                else:
                    temp.append(element)
            if isinstance(node, ast.Module):
                temp = temp[:-3]
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



img_path = os.path.join(os.path.curdir, "png")
if os.path.isdir(img_path):
    shutil.rmtree(img_path)
os.mkdir(img_path)
namespace = {}
src = Handler(text)
exec(compile(src.processed, filename="<src>", mode="exec"), namespace)
