# Recursively reverse a linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0 

    def isEmpty(self):
        if self.count == 0:
            return True
        return False
    
    def addnode(self,data):
        new = Node(data)
        if self.isEmpty():
            self.head = new
            self.tail = new
            self.count += 1
        else:
            new.next = self.head
            self.head = new
            self.count += 1

    def show(self):
        list = ''
        ptr = self.head
        while ptr:
            list += str(ptr.data)
            list += '->'
            ptr = ptr.next
        print list
    
    def reverse(self,cur):
        cur = cur
        n = cur.next

        if n.next:
            self.reverse(cur.next)
            n.next = cur
            cur.next = None
        else:
            n.next = cur
            self.head = n

def main():
    L = LinkedList()
    L.addnode(89)
    L.addnode(67)
    L.addnode(21)
    L.addnode(32)
    L.addnode(2)
    L.show()
    L.reverse(L.head)
    L.show()


if __name__ == '__main__':
    main()
