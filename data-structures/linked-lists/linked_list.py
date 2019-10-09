# Python Implementation of a Linked List (keeping all native list methods)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.first = None
        self._size = 0
        self._curr = None

    def append(self, item):
        self.insert(self._size, item)

    def insert(self, index, item):
        if index > self._size:
            raise IndexError
        self._size += 1
        if self.first is None:
            self.first = Node(item)
            return
        prev = None
        curr = self.first
        while index != 0:
            prev = curr
            curr = curr.next
            index -=1
        new_node = Node(item)
        new_node.next = curr
        if prev is not None:
            prev.next = new_node

    def extend(self, items):
        if self.first is None and len(items): # ensure this node is not created unnecessarily
            self.first = Node(None)
        curr = self.first
        while curr.next is not None:
            curr = curr.next
        for item in items:
            curr.next = Node(None)
            curr.value = item
            curr = curr.next
            self._size += 1
        curr.next = None
    
    def sum(self):
        total = 0
        for node in self:
            total += node.value
        return total
    
    def count(self, item):
        total = 0
        for node in self:
            if node.value == item:
                total += 1
        return total


    def index(self, item, start = 0, end = None):
        if end is None:
            end = self._size
        if end > self._size or start > end:
            raise IndexError
        i = 0
        curr = start.first
        while i < start:
            i += 1
            curr = curr.next
        while i < end:
            if curr.value == item:
                return i
            i += 1
            curr = curr.next
        return -1

    def pop(self, index):
        if index > self._size:
            raise IndexError
        if index == 0:
            temp, self.first = self.first, self.first.next
            return temp
        prev = None
        curr = self.first
        while index > 0:
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return curr.value

    def remove(self, item):
        prev = None
        curr = self.first
        while curr is not None:
            if curr.value == item:
                prev.next = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def __iter__(self):
        self._curr = self.first
        return self

    def __next__(self):
        if self._curr is None:
            raise StopIteration
        val = self._curr.value
        self._curr = self._curr.next
        return val

    def __len__(self):
        return self._size
        
    def __str__(self):
        curr = self.first
        string = ''
        while curr is not None:
            string += str(curr.value) + ', '
            curr = curr.next
        if len(string) > 0:
            string = string[:-2] # get rid of last comma
        return '[' + string + ']'

# if __name__ == '__main__':
#     a = LinkedList()
#     for i in range(5):
#         a.append(i)
#     for i in a:
#         print(i)