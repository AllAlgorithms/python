
class Node:
    def __init__(self,_data,_next=None):
        self.data = _data
        self.next = _next
    
    def __str__(self):
        return f"Node({self.data})"


class Stack:

    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, _data):
        node = Node(_data)
        node.next = self.top
        self.top = node

    def pop(self):
        if self.isEmpty() is not None:
            returnValue = self.top
            self.top = self.top.next
            return returnValue

    def __str__(self):
        res = ""
        node = self.top
        while node:
            res += str(node.data) + " | "
            node = node.next
        return res[::-1]


if __name__ == "__main__":
    s = Stack()
    s.push(8)
    s.push(4)
    print(s)
    s.pop()
    s.push(11)
    s.push(3)
    print(s)
