from lolviz import *
import tempfile
from stack import *
from linked_list import *
from d_linked_list import *
from bstree import *


def view_graph(graph):
    # render to a different file for each invocation
    graph.format = 'svg'
    graph.view(tempfile.mktemp('.gv'))


def list_example():
    # listviz on list
    lst = ['hi','mom',{3,4},{"parrt":"user"}]
    g = listviz(lst)
    view_graph(g)
    lst = []
    g = listviz(lst)
    view_graph(g)


def stack_example():
    # objviz on stack using a list
    sk = Stack()
    g = objviz(sk)
    view_graph(g)
    sk.push(1)
    sk.push(2)
    sk.push(3)
    sk.push(4)
    sk.push(5)
    g = objviz(sk)
    view_graph(g)
    sk.pop()
    sk.pop()
    sk.pop()
    g = objviz(sk)
    view_graph(g)


def linkedlist_example():
    # objviz on linkedlist
    ll = SLinkedList()
    ll.add_first('a')
    ll.add_first('b')
    ll.add_first('c')
    ll.add_last('1')
    ll.add_last('2')
    ll.add_last('3')
    g = objviz(ll)
    view_graph(g)
    ll.remove_first()
    ll.remove_last()
    g = objviz(ll)
    view_graph(g)


def d_linkedlist_example():
    # objviz on double linked list
    dll = DLinkedList()
    dll.add_first(1)
    dll.add_first(2)
    dll.add_last(3)
    dll.add_last(4)
    g = treeviz(dll)
    view_graph(g)
    g = objviz(dll)
    view_graph(g)


def bst_example():
    # treeviz on binary search tree
    bst = BSTNode()
    bst.insert(5)
    bst.insert(7)
    bst.insert(3)
    bst.insert(1)
    bst.insert(2)
    bst.insert(4)
    bst.insert(8)
    g = treeviz(bst)
    view_graph(g)
    bst.delete(3)
    g = treeviz(bst)
    view_graph(g)



def call_example():
    # callsviz on variables
    x = 5
    value = 99
    data = ['value','x','data']
    g = callsviz()
    view_graph(g)
    g = callsviz(varnames=['value','x','data'])
    view_graph(g)


if __name__ == '__main__':
    list_example()
    stack_example()
    call_example()
    linkedlist_example()
    d_linkedlist_example()
    bst_example()
    pass