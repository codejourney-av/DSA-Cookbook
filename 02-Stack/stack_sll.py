# Node class to represent each element in the stack
class Node:
    def __init__(self, data=None, next=None):
        self.data = data    # Value stored in the node
        self.next = next    # Pointer to the next node (link)


# Stack implementation using Singly Linked List
class Stack:
    def __init__(self):
        self.top = None          # Points to the top (last pushed) node
        self.data_count = 0      # Keeps track of number of elements in the stack

    # Check if the stack is empty
    def is_empty(self):
        return self.top is None

    # Push an element onto the stack
    def push(self, data):
        new_node = Node(data)    # Create a new node
        new_node.next = self.top # Link new node to the current top
        self.top = new_node      # Update top to new node
        self.data_count += 1     # Increase size count

    # Pop (remove) the top element from the stack
    def pop(self):
        if self.is_empty():
            return "Error: Stack is empty"
        popped_data = self.top.data    # Get the data from the top node
        self.top = self.top.next       # Move top pointer to next node
        self.data_count -= 1           # Decrease size count
        return popped_data

    # Peek (see) the top element without removing it
    def peek(self):
        if self.is_empty():
            return "Error: Stack is empty"
        return self.top.data

    # Return the number of elements in the stack
    def size(self):
        return self.data_count


# Example usage (only for testing/demo purposes)
if __name__ == "__main__":
    s = Stack()
    s.push(44)
    s.push(55)
    s.push(33)
    s.push(11)

    print("Popped data:", s.pop())      # Should remove 11
    print("Peek data:", s.peek())       # Should show 33
    print("Total size of stack:", s.size())  # Should be 3
