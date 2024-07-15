class Stack:
    """
    Represents a stack data structure using a list.
    """
    def __init__(self):
        # Initializes an empty stack.
        self.items = []

    def is_empty(self):
        # Checks if the stack is empty
        return self.items == []

    def push(self, item):
        # Adds item to the top of the stack
        self.items.append(item)

    def pop(self):
        # Removes and returns the item from the top of the stack
        if self.is_empty():
            raise IndexError('Pop from an empty stack')
        return self.items.pop()

    def peek(self):
        # Returns the item at the top of the stack without removing it.
        if self.is_empty():
            raise IndexError('Peek from an empty stack')
        return self.items[-1]

    def size(self):
        # Returns the number of items in the stack.
        return len(self.items)






