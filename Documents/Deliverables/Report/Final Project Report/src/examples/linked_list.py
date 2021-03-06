class SLLNode:
    def __init__(self, item, nextnode):
        self.element = item #any object
        self.next = nextnode

class SLinkedList:
    def __init__(self):
        self.first = None #an SLLNode
        self.size = 0

    def add_first(self, element):
        newnode = SLLNode(element, self.first)
        self.first = newnode
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
        newnode = SLLNode(element, None)
        if self.first == None:
            self.first = newnode
        else:
            n = self.first
            while n.next:
                n = n.next
            n.next = newnode
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

ll = SLinkedList()
ll.add_first('a')
ll.add_first('b')
ll.add_first('c')
ll.add_last('1')
ll.add_last('2')
ll.add_last('3')
ll.remove_first()
ll.remove_last()

