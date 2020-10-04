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

    def add_node(self,data):
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
            print ptr.data
            print ' -> '
            ptr = ptr.next
        print list
    
    def middle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print slow.data


def main():
    L = LinkedList()
    L.add_node(2)
    L.add_node(32)
    L.add_node(21)
    L.add_node(67)
    L.add_node(89)
    L.middle()
if __name__ == '__main__':
    main()
