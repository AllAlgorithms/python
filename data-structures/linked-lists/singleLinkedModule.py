# The program that creates a single link list of true values 
# and implements the actions outlined in the link list.

class LinkedList:
    class ListNode:
        def __init__(self, data, next= None):
            self.info = data
            self.next = next

        def getInfo(self):
            return self.info
        
        def setInfo(self, value):
            self.info = value

        def getNext(self):
            return self.next

        def setNext(self, ptr):
            self.next = ptr #end of listNode class

    def __init__(self):
        self.head = None
        self.last = None
        self.size = 0

    def __del__(self):
        current = self.head
        while current:
            ptr = current
            current = current.next
            del ptr
        
    def getSize(self):
        return self.size
    def isEmpty(self):
        return self.head == None

#Search Node 

    def searchNode(self, data):
        if (self.isEmpty()):
            return None
        else:
            ptr = self.head
            found = False
            while ptr and found  is False:
                if ptr.getInfo() == data:
                    found == True
                else: 
                    ptr == ptr.getNext()
        return ptr

    def insertAtFirst(self, ptr):
        self.head = ptr 
        self.size += 1
        if self.getSize() == 1:
            self.last = self.head
        return True

    def insertAfterNode(self, ptr):
        if (self.isEmpty()):
            self.head = self.last = ptr
        else:
            self.last.next = ptr
            self.last = ptr
        self.size += 1
    
    def deleteNode(self, data):
        current = self.head 
        pre = None
        found = False
        while current and found is False:
            if current.getInfo() == data:
                found = True
            else:
                pre = current
                current = current.getNext()
        if found:
            if current == self.head: #first Node deleted
                self.head = current.next 
                del current
            else:
                pre.next = current.next
                current.next = None
                del current #current = None
            self.size -= 1 
        return found

    def traverse(self):
        if (self.isEmpty() != True):
            ptr = self.head
            while ptr: 
                print(ptr.info, end = "\n")
                ptr = ptr.getNext()
                
                        
