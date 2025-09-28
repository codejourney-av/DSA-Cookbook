class Stack(list):
    """
    Stack implementation by inheriting from Python's built-in list.
    Follows LIFO (Last In, First Out) principle.
    """

    def __init__(self):
        # Initialize the parent list
        super().__init__()

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self) == 0

    def push(self, data):
        """Push (add) an element to the top of the stack"""
        self.append(data)

    def pop(self):
        """Pop (remove) the top element from the stack"""
        if self.is_empty():
            return "Error: stack is empty!"
        return super().pop()  # Call list.pop()

    def peek(self):
        """View the top element without removing it"""
        if self.is_empty():
            return "Error: stack is empty!"
        return self[-1]

    def size(self):
        """Return the number of elements in the stack"""
        return len(self)

    def insert(self, index, data):
        """
        Disable insert method to maintain stack behavior.
        Prevents inserting at arbitrary positions.
        """
        raise AttributeError("insert method is disabled for Stack")

        
# Example usage
if __name__ == "__main__":
    s = Stack()
    s.push(34)
    s.push(33)
    s.push(88)

    print("Popped:", s.pop())         # 88
    print("Top element:", s.peek())   # 33
    print("Size:", s.size())          # 2
    print("Is empty:", s.is_empty())  # False

    # This will raise an AttributeError
    # print(s.insert(2, 99))
