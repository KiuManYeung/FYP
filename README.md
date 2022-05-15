# Animation Environment for Linked Data Struccture

## Python Visualiser
The basis of this project is to provide data structures visualisation for educational purpose, which students can inspect their code to achieve better learning result.  The main goal of the project is to create a software that shows step-by-step execution of computer algorithms on data manipulations in Python.  The software provides a graphical interface that allows users to input code implementation and display a stepped animation of the execution beside.

## The architecture
The software is implemented in Python.  The GUI is built with tkinter, providing a textbox for code input, a canvas for graph display, buttons to execute and traveling between steps.  One main component of the tool is parsing.  Abstract syntax tree(AST) allows the tool to give structural representation of the code input.  The idea is to insert graphing commands into appropriate places using AST to the source code before executing.  The inserts trigger the visualisation tool, Graphviz and Lolviz, to create graphical presentations of the data structure.  It has capability to show abstract data structures with pointers.

## Run Visualizer
```
cd src
python app.py
```
Running the script requires the installation of [Graphviz](https://graphviz.org/), [Graphviz interface for Python](https://github.com/xflr6/graphviz) and [Lolviz](https://github.com/parrt/lolviz).
