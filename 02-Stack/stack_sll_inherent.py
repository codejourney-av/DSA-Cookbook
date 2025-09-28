# stack_with_inheritance.py

class Node:
    """A node in the singly linked list."""
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class SLL:
    """Singly Linked List with basic insertion and deletion methods."""
    def __init__(self):
        self.start = None

    def insert_at_first(self, data):
        """Insert a node at the beginning of the linked list."""
        new_node = Node(data, self.start)
        self.start = new_node

    def delete_at_first(self):
        """Delete the first node of the linked list."""
        if self.start is None:
            return None
        removed_data = self.start.data
        self.start = self.start.next
        return removed_data

    def traverse(self):
        """Return all elements of the linked list as a list."""
        elements = []
        current = self.start
        while current:
            elements.append(current.data)
            current = current.next
        return elements


class Stack(SLL):
    """Stack implementation using inheritance from Singly Linked List (SLL)."""
    def __init__(self):
        super().__init__()
        self.count = 0

    def is_empty(self):
        return self.start is None

    def push(self, data):
        """Push element onto stack (insert at beginning of list)."""
        self.insert_at_first(data)
        self.count += 1

    def pop(self):
        """Pop element from stack (delete from beginning of list)."""
        if not self.is_empty():
            popped = self.delete_at_first()
            self.count -= 1
            return popped
        return "Error: Stack is empty"

    def peek(self):
        """Return the top element without removing it."""
        if not self.is_empty():
            return self.start.data
        return "Error: Stack is empty"

    def size(self):
        """Return the number of elements in the stack."""
        return self.count


if __name__ == "__main__":
    s = Stack()
    print("Is stack empty?", s.is_empty())
    s.push(88)
    s.push(99)
    s.push(44)
    s.push(21)

    print("Stack elements (top → bottom):", s.traverse())
    print("Peek:", s.peek())
    print("Popped:", s.pop())
    print("Peek after pop:", s.peek())
    print("Stack size:", s.size())
