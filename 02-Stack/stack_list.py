# Stack implementation using Python List
# --------------------------------------
# Concept:
# A Stack is a linear data structure that works on LIFO (Last In, First Out).
# Think of it like a stack of plates: the last plate placed on top
# will be the first one removed.

class Stack:
    def __init__(self):
        # We'll use a Python list internally to hold stack elements
        self.items = []

    def is_empty(self):
        # Return True if stack has no elements
        return len(self.items) == 0

    def push(self, data):
        # Add an element to the top of the stack
        self.items.append(data)

    def pop(self):
        # Remove and return the top element from the stack
        if self.is_empty():
            return "Error: Stack Underflow (nothing to pop)"
        return self.items.pop()

    def peek(self):
        # Return the top element without removing it
        if self.is_empty():
            return "Error: Stack is empty!"
        return self.items[-1]

    def size(self):
        # Return the total number of elements in the stack
        return len(self.items)

    def print_stack(self):
        # Display stack elements (from bottom to top)
        if self.is_empty():
            return "Error: Nothing to print, stack is empty!"
        return self.items


# Example usage
if __name__ == "__main__":
    s = Stack()
    
    s.push(90)
    s.push(20)
    s.push(48)
    s.push(33)

    print("Top element (peek):", s.peek())
    print("\nPopped element:", s.pop())
    print("\nSize of stack:", s.size())
    print("\nIs stack empty?:", s.is_empty())
    print("\nTop element after pop (peek):", s.peek())
    print("\nStack elements:", s.print_stack())
