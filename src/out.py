from lolviz import *
import os
global png_counter
png_counter = 0
global graph_lines
graph_lines = []

class BSTNode:
    global png_counter
    global graph_lines

    def __init__(self, val=None):
        global png_counter
        global graph_lines
        self.left = None
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        self.right = None
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        self.val = val
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))

    def insert(self, val):
        global png_counter
        global graph_lines
        if not self.val:
            self.val = val
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            return
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.val == val:
            return
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if val < self.val:
            if self.left:
                self.left.insert(val)
                mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
                mySpecialGraph.format = 'png'
                png_counter += 1
                mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
                return
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            self.left = BSTNode(val)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            return
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.right:
            self.right.insert(val)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            return
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        self.right = BSTNode(val)
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))

    def get_min(self):
        global png_counter
        global graph_lines
        current = self
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        while current.left is not None:
            current = current.left
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return current.val

    def get_max(self):
        global png_counter
        global graph_lines
        current = self
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        while current.right is not None:
            current = current.right
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return current.val

    def delete(self, val):
        global png_counter
        global graph_lines
        if self == None:
            return self
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if val < self.val:
            if self.left:
                self.left = self.left.delete(val)
                mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
                mySpecialGraph.format = 'png'
                png_counter += 1
                mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            return self
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if val > self.val:
            if self.right:
                self.right = self.right.delete(val)
                mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
                mySpecialGraph.format = 'png'
                png_counter += 1
                mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            return self
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.right == None:
            return self.left
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.left == None:
            return self.right
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        min_larger_node = self.right
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        self.val = min_larger_node.val
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        self.right = self.right.delete(min_larger_node.val)
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return self

    def exists(self, val):
        global png_counter
        global graph_lines
        if val == self.val:
            return True
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if val < self.val:
            if self.left == None:
                return False
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
            return self.left.exists(val)
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.right == None:
            return False
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return self.right.exists(val)

    def preorder(self, vals):
        global png_counter
        global graph_lines
        if self.val is not None:
            vals.append(self.val)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.left is not None:
            self.left.preorder(vals)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.right is not None:
            self.right.preorder(vals)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return vals

    def inorder(self, vals):
        global png_counter
        global graph_lines
        if self.left is not None:
            self.left.inorder(vals)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.val is not None:
            vals.append(self.val)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.right is not None:
            self.right.inorder(vals)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return vals

    def postorder(self, vals):
        global png_counter
        global graph_lines
        if self.left is not None:
            self.left.postorder(vals)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.right is not None:
            self.right.postorder(vals)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        if self.val is not None:
            vals.append(self.val)
            mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
            mySpecialGraph.format = 'png'
            png_counter += 1
            mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
        mySpecialGraph.format = 'png'
        png_counter += 1
        mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
        return vals
insert = [5, 7, 3, 1, 2, 4, 8]
mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
delete = [3, 1, 5, 7, 2]
mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
bst = BSTNode()
mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
mySpecialGraph.format = 'png'
png_counter += 1
mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))
for i in insert:
    bst.insert(i)
    mySpecialGraph = callsviz(varnames=['val', 'insert', 'min_larger_node', 'i', 'self', 'current', 'vals', 'delete', 'BSTNode', 'bst'])
    mySpecialGraph.format = 'png'
    png_counter += 1
    mySpecialGraph.render(os.path.join(os.path.curdir, 'png', str(png_counter).zfill(4)))