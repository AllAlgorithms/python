class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
    
class DoublyLinkedList:
    def __init__(self, object):
        self.tail = self.head = Node(object)
    
    def append(self, object):
        c = self.tail
        self.tail.next = Node(object)
        self.tail = self.tail.next
        self.tail.prev = c
    
    def insert(self, index, object):
        new_node = Node(object)
        if index == 0:
            ll = new_node
            self.head.prev = ll
            ll.next = self.head
            self.head = ll
        else:
            current_indx = 0
            ll = self.head
            while current_indx < index - 1:
                ll = ll.next
                current_indx += 1
            ll.next.prev = new_node
            new_node.next = ll.next
            ll.next = new_node
            new_node.prev = ll
    
    def pop(self):
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
        self.tail = curr
        self.tail.next = None
    
    def show(self, reverse = False):
        if reverse:
            curr = self.tail
            while curr:
                print(curr.value)
                curr = curr.prev
        else:
            curr = self.head
            while curr:
                print(curr.value)
                curr = curr.next
