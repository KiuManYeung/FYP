import ast
from astpretty import pformat

with open("fibo.py", 'r') as file:
    text = file.read()
with open("out.py", 'w') as out:
    # out.write(ast.unparse(src.processed))
    out.write(pformat(ast.parse(text), show_offsets=False))