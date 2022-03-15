class SLLNode:
    def __init__(self, item, nextnode):
        self.element = item #any object
        self.next = nextnode

class SLinkedList:
    def __init__(self):
        self.first = None #an SLLNode
        self.size = 0

    def add_first(self, element):
        node = SLLNode(element, self.first)
        self.first = node
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
            node = self.first
            while node.next:
                node = node.next
            node.next = newnode
            self.size = self.size + 1

    def get_last(self):
        if self.size == 0:
            return None
        node = self.first
        while node.next:
            node = node.next
        return node.element

    def remove_last(self):
        if self.size == 0:
            return None
        node = self.first
        while node.next.next:
            node = node.next
        node.next = None
        self.size = self.size - 1

    def length(self):
        return self.size