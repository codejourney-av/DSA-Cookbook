"""
Stack Implementation in Python using List Inheritance
Description:
This module defines a Stack class that inherits from Python's built-in list.
It provides stack-specific methods such as push, pop, peek, and size
while restricting operations that violate stack principles (e.g., insert).
"""

class Stack(list):
    def __init__(self):
        super().__init__()  # Initialize the list properly

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self) == 0

    def push(self, data):
        """Add an element to the top of the stack."""
        self.append(data)

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            return "Error: Stack is empty"
        return super().pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return "Error: Stack is empty"
        return self[-1]

    def size(self):
        """Return the number of elements in the stack."""
        return len(self)

    def insert(self, index, data):
        """Disable the insert method to enforce stack behavior."""
        raise AttributeError("Insert operation not allowed in Stack")

# ---- Driver Code ---- #
if __name__ == "__main__":
    s = Stack()
    s.push(34)
    s.push(33)
    s.push(88)

    print("Popped:", s.pop())        # Removes 88
    print("Top element:", s.peek())  # Shows 33
    print("Size:", s.size())         # 2
    print("Is empty:", s.is_empty()) # False

    try:
        s.insert(2, 99)
    except AttributeError as e:
        print(e)
