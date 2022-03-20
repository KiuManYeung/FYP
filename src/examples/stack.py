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