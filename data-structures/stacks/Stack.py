class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self._first = None
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def push(self, item):
        new_node = Node(item)
        if self._first is None:
            self._first = new_node
        else:
            new_node.next = self._first
        self._size += 1
    
    def pop(self):
        if self._first is None:
            raise IndexError
        val = self._first.value
        self.first = self.first.next
        self._size -= 1
        return val
        