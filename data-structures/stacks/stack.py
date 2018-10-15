
class Stack:
    """
    Implentation of the Stack abstract data type. LIFO.
    """
    def __init__(self):
        # Constructur for the Stack
        self.items = list()

    def __str__(self):
        # Printable
        if not self.items:
            return "~( )~"
        else:
            items_str = ", ".join(str(i) for i in self.items)
            return f"~({items_str})~"

    def push(self, item):
        """
        Pushes item to the top of the Stack.
        """
        self.items.append(item)

    def empty(self):
        """
        Returns True if the Stack is empty.
        """
        return not self.items

    def pop(self):
        """
         Removes item from the top of the Stack.
         """
        if not self.items:
            return "The Stack is empty."
        else:
            return self.items.pop()

    def peek_top(self):
        """
         Returns the top item of the Stack.
         """
        return self.items[len(self.items)-1]

    def peek_base(self):
        """
         Returns the base item of the Stack.
         """
        return self.items[0]

    def size(self):
        """
         Returns the number of items in the Stack.
         """
        return len(self.items)

    def clear(self):
        """
        Deletes all items in the Stack.
        """
        self.items = list()
        return "All items deleted"
