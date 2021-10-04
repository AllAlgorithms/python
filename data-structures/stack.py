


class Stack:

    def __init__(self, size):
        self.size = size
        self.top = -1
        self.arr = [0]*size

    def isEmpty(self):
        return self.top == -1

    def isFull(self):
        return self.top == self.size-1

    def push(self, value):
        if not self.isFull():
            self.top += 1
            self.arr[self.top] = value

    def pop(self):
        if not self.isEmpty():
            self.top -= 1

    def show(self):
        for i in range(self.top):
            print(self.arr[i], end=", ")
        if not self.isEmpty():
            print(self.arr[self.top])


if __name__ == "__main__":
    s = Stack(10)
    s.push(8)
    s.push(4)
    s.pop()
    s.push(11)
    s.push(3)
    s.show()
