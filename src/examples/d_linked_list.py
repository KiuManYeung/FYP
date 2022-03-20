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
        node = DLLNode(element, None, self.first)
        if self.first:
            node.next.prev = node
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
        if self.first == None:
            self.first = DLLNode(element, None, None)
        else:
            node = self.first
            while node.next:
                node = node.next
            node.next = DLLNode(element, node, None)
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