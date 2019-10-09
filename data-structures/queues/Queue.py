class QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self._first = None
        self._last = None
        self._size = 0

    def enqueue(self, item):
        if self._first is None:
            self._first = QueueNode(item)
            self._last = self._first
        else:
            new_node = QueueNode(item)
            new_node.next = self._first
            self._first.prev = new_node
        self._size += 1

    def dequeue(self):
        if self._size <= 0:
            raise IndexError
        val = self._last.value
        self._last = self._last.prev
        if self._last is not None:
            self._last.next = None
        self._size -= 1
        return val

    def __len__(self):
        return self._size
