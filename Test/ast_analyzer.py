import ast
from pprint import pprint

# class Analyzer(ast.NodeVisitor):
#     def __init__(self):
#         self.stats = {"import": [], "from": []}

#     def visit_Import(self, node):
#         for alias in node.names:
#             self.stats["import"].append(alias.name)
#         self.generic_visit(node)

#     def visit_ImportFrom(self, node):
#         for alias in node.names:
#             self.stats["from"].append(alias.name)
#         self.generic_visit(node)

#     def report(self):
#         pprint(self.stats)


class Analyzer(ast.NodeVisitor):

    def __init__(self):
        self.stats = {"import": [], "from": []}
        
    def visit_Import(self,node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_ImportFrom(self,node):
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Assign(self,node):
        print('Node type: Assign and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)
    
    def visit_BinOp(self, node):
        print('Node type: BinOp and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Expr(self, node):
        print('Node type: Expr and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Num(self,node):
        print('Node type: Num and fields: ', node._fields)

    def visit_Name(self,node):
        print('Node type: Name and fields: ', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def visit_Str(self, node):
        print('Node type: Str and fields: ', node._fields)

    def visit_Assert(self, node):
        print('Node type: Assert\nFields:', node._fields)
        ast.NodeVisitor.generic_visit(self, node)

    def report(self):
        pprint(self.stats)