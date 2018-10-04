# Python Implementation of a Linked List

class Node(object):
    def __init__(self, value):
        super(Node, self).__init__()

        self._value = value
        self._next = None

    def traverse(self):
        node = self
        while node:
            print(node._value)
            node = node._next

### Test ###

node_1 = Node(123)
node_2 = Node('abc')
node_3 = Node('Linked List')

node_1._next = node_2
node_2._next = node_3

node_1.traverse()
