"""
Queue Implementation in Python using Linked List

Description:
This module defines a Queue data structure following the FIFO (First In, First Out) principle.
It uses a linked list internally for efficient enqueue and dequeue operations.
"""

class Node:
    """A Node in a linked list."""
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class Queue:
    """A Queue implemented using a linked list."""
    def __init__(self):
        self.front = None
        self.rear = None
        self.count = 0

    def is_empty(self):
        """Check if the queue is empty."""
        return self.front is None

    def enqueue(self, data):
        """Add an element to the rear of the queue."""
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node
        self.count += 1

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue.")
        
        removed_node = self.front
        self.front = self.front.next_node
        if self.front is None:
            self.rear = None
        self.count -= 1
        return removed_node.data

    def get_front(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty. No front element.")
        return self.front.data

    def get_rear(self):
        """Return the rear element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty. No rear element.")
        return self.rear.data

    def display(self):
        """Display all elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
            return
        current = self.front
        while current:
            print(current.data, end=" <- ")
            current = current.next_node
        print("None")

    def size(self):
        """Return the number of elements in the queue."""
        return self.count


# ---- Example Usage ---- #
if __name__ == "__main__":
    q = Queue()
    print("Is queue empty?", q.is_empty())

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("\nInitial queue:")
    q.display()

    try:
        print(f"\nFront element: {q.get_front()}")
        print(f"Rear element: {q.get_rear()}")
    except IndexError as e:
        print(e)

    print("\nDequeuing one element:", q.dequeue())
    print("Queue after one dequeue:")
    q.display()

    print(f"\nFront element: {q.get_front()}")
    print(f"Rear element: {q.get_rear()}")
