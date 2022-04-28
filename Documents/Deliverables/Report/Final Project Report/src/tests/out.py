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
    execution_sequence.append((1, 1))
    mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
    if n <= 1:
        execution_sequence.append((2, 1))
        mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        execution_sequence.append((3, 0))
        return n
    else:
        execution_sequence.append((4, 1))
        mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return recur_fibo(n - 1) + recur_fibo(n - 2)
        execution_sequence.append((5, 0))
execution_sequence.append((7, 1))
nterms = 3
mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
if nterms <= 0:
    execution_sequence.append((10, 1))
    mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
    execution_sequence.append((11, 1))
    print('Plese enter a positive integer')
    mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
else:
    execution_sequence.append((12, 1))
    mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
    print('Fibonacci sequence:')
    mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
    execution_sequence.append((13, 1))
    for i in range(nterms):
        execution_sequence.append((14, 1))
        mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        execution_sequence.append((15, 1))
        print(recur_fibo(i))
        mySpecialGraph = callsviz(varnames=['nterms', 'i', 'print', 'n', 'recur_fibo', 'range'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
    execution_sequence.append((14, 0))