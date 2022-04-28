from lolviz import *
import os
global png_counter
png_counter = 0
global execution_sequence
execution_sequence = []
execution_sequence.append((1, 0))

def recur_fibo(n):
    global png_counter
    global execution_sequence
    execution_sequence.append((2, 1))
    if n <= 1:
        execution_sequence.append((3, 0))
        return n
    else:
        return recur_fibo(n - 1) + recur_fibo(n - 2)
    mySpecialGraph = callsviz(varnames=['i', 'range', 'n', 'recur_fibo', 'print', 'nterms'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
execution_sequence.append((7, 1))
nterms = 10
mySpecialGraph = callsviz(varnames=['i', 'range', 'n', 'recur_fibo', 'print', 'nterms'])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
execution_sequence.append((10, 1))
if nterms <= 0:
    execution_sequence.append((11, 1))
    print('Plese enter a positive integer')
    mySpecialGraph = callsviz(varnames=['i', 'range', 'n', 'recur_fibo', 'print', 'nterms'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
else:
    print('Fibonacci sequence:')
    for i in range(nterms):
        print(recur_fibo(i))
mySpecialGraph = callsviz(varnames=['i', 'range', 'n', 'recur_fibo', 'print', 'nterms'])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))