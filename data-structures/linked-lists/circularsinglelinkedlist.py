class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
 
class CircularLinkedList:
    def __init__(self):
        self.head = None
 
    def get_node(self, index):
        if self.head is None:
            return None
        current = self.head
        for i in range(index):
            current = current.next
            if current == self.head:
                return None
        return current
 
    def get_prev_node(self, ref_node):
        if self.head is None:
            return None
        current = self.head
        while current.next != ref_node:
            current = current.next
        return current
 
    def insert_after(self, ref_node, new_node):
        new_node.next = ref_node.next
        ref_node.next = new_node
 
    def insert_before(self, ref_node, new_node):
        prev_node = self.get_prev_node(ref_node)
        self.insert_after(prev_node, new_node)
 
    def insert_at_end(self, new_node):
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
        else:
            self.insert_before(self.head, new_node)
 
    def insert_at_beg(self, new_node):
        self.insert_at_end(new_node)
        self.head = new_node
 
    def remove(self, node):
        if self.head.next == self.head:
            self.head = None
        else:
            prev_node = self.get_prev_node(node)
            prev_node.next = node.next
            if self.head == node:
                self.head = node.next
 
    def display(self):
        if self.head is None:
            return
        current = self.head
        while True:
            print(current.data, end = ' ')
            current = current.next
            if current == self.head:
                break
 
 
a_cllist = CircularLinkedList()
 
print('Menu')
print('insert <data> after <index>')
print('insert <data> before <index>')
print('insert <data> at beg')
print('insert <data> at end')
print('remove <index>') 
print('quit')
 
while True:
    print('The list: ', end = '')
    a_cllist.display()
    print()
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
 
    if operation == 'insert':
        data = int(do[1])
        position = do[3].strip().lower()
        new_node = Node(data)
        suboperation = do[2].strip().lower() 
        if suboperation == 'at':
            if position == 'beg':
                a_cllist.insert_at_beg(new_node)
            elif position == 'end':
                a_cllist.insert_at_end(new_node)
        else:
            index = int(position)
            ref_node = a_cllist.get_node(index)
            if ref_node is None:
                print('No such index.')
                continue
            if suboperation == 'after':
                a_cllist.insert_after(ref_node, new_node)
            elif suboperation == 'before':
                a_cllist.insert_before(ref_node, new_node)
 
    elif operation == 'remove':
        index = int(do[1])
        node = a_cllist.get_node(index)
        if node is None:
            print('No such index.')
            continue
        a_cllist.remove(node)
 
    elif operation == 'quit':
        break