import ast, astor
from ast_analyzer import Analyzer
from astpretty import pprint

def insert_statement(tree, statement):
    if hasattr(tree, 'body'):
        result = [statement] * (len(tree.body) * 2 - 1)
        result[0::2] = tree.body
        tree.body = result
        for element in tree.body:
            insert_statement(element, statement)
    # if hasattr(tree, 'orelse'):
    #     tree.orelse.insert(1, statement)
    #     insert_statement(tree.orelse, statement)


def main():
    with open("ast_example.py", "r") as source:
        tree = ast.parse(source.read())

    # analyzer = Analyzer()
    # analyzer.visit(tree)
    # analyzer.report()
    print()

    pprint(tree, show_offsets=False)
    print()

    exec(compile(tree, filename="<ast>", mode="exec"))

    # Create print statement
    message = ast.Str("------------------------------")
    print_func = ast.Name("print", ast.Load())
    print_call = ast.Call(print_func, [message], []) # add two None args in Python<=3.4
    print_statement = ast.Expr(print_call)
    # Insert print statement to 1
    # tree.body.insert(1, print_statement)
    # tree.body[0].body.insert(1, print_statement)

    # Insert new statement after every statement
    insert_statement(tree, print_statement)

    # Print and execute new tree
    source = astor.to_source(tree)
    print(source)
    exec(compile(source, filename="<ast>", mode="exec"))
    


if __name__ == "__main__":
    main()