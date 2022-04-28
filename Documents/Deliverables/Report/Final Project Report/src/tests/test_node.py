import ast


code = """
from lolviz import *
class Foo:
    def __init__(self):
        self.n = 1
        g = callsviz()
        g.view()

node = Foo()
g = callsviz()
g.view()
"""

tree = ast.parse(code)
exec(ast.unparse(tree))