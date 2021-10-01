class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Queue():
    def __init__(self):
        self.tail = self.head = None
        self.length = 0
    
    def insert(self, object):
        if self.length == 0:
            self.tail = self.head = Node(object)
        else:
            c = Node(object)
            self.head.prev = c
            c.next = self.head
            self.head = c
        self.length += 1

    def pop(self):
        if self.length == 1:
            value = self.tail.data
            self.tail = self.head = None
        else:
            c = self.tail.prev
            value = self.tail.data
            c.next = None
            self.tail = c
        self.length -= 1
        return value

    def isEmpty(self):
        return not bool(self.length)
        
    def show(self):
        curr = self.head
        lst = []
        while curr:
            lst.append(curr.data)
            curr = curr.next
        return lst