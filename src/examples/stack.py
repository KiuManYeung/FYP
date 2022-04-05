class Stack:
    def __init__(self):
        self.alist = []

    def push(self, element):
        self.alist.append(element) 

    def pop(self):
        if len(self.alist) == 0:
            return None
        return self.alist.pop()

    def top(self):
        if len(self.alist) == 0:
            return None 
        return self.alist[-1]

    def length(self):
        return len(self.alist)

insert = [5,7,3,1,2,4,8]

bst = Stack()
for i in insert:
    bst.push(i)
for i in range(len(insert)):
    bst.pop()