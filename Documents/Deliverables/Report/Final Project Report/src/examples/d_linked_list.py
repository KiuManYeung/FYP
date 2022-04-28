# example of remove implemented incorrectly

class DLLNode:
    def __init__(self, item, prevnode, nextnode):
        self.element = item
        self.next = nextnode
        self.prev = prevnode


class DLinkedList:
    def __init__(self):
        self.first = None
        self.size = 0

    def add_first(self, element):
        n = DLLNode(element, None, self.first)
        if self.first:
            n.next.prev = n
        self.first = n
        self.size = self.size + 1

    def get_first(self):
        if self.size == 0:
            return None
        return self.first.element

    def remove_first(self):
        if self.size == 0:
            return None
        item = self.first.element
        self.first = self.first.next
        self.size = self.size - 1
        return item

    def add_last(self, element):
        if self.first == None:
            self.first = DLLNode(element, None, None)
        else:
            n = self.first
            while n.next:
                n = n.next
            n.next = DLLNode(element, n, None)
            self.size = self.size + 1

    def get_last(self):
        if self.size == 0:
            return None
        n = self.first
        while n.next:
            n = n.next
        return n.element

    def remove_last(self):
        if self.size == 0:
            return None
        n = self.first
        while n.next.next:
            n = n.next
        n.next = None
        self.size = self.size - 1

    def length(self):
        return self.size

insert = [5,7,3,1,2,4,8]

dll = DLinkedList()
for i in insert:
    if (i % 2) == 0:
        dll.add_last(i)
    else:
        dll.add_last(i)
for i in range(len(insert)):
    if (i % 2) == 0:
        dll.remove_first()
    else:
        dll.remove_last()