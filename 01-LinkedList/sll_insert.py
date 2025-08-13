#  Singly Linked List - Insertion Operations

class Node:
    def __init__(self, data=None, next=None):
        # Each node just has two parts: data and a pointer (next)
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        # 'start' will always point to the first node (head) of the list
        self.start = start

    def is_empty(self):
        # Quick check if the list is empty
        if self.start is None:
            print('Linked list is empty, please enter some values.')
            return True
        return False

    def insert_at_first(self, data):
        # Create a new node
        new_node = Node(data)
        # Link this new node to the current first node
        new_node.next = self.start
        # Update 'start' so it now points to the new node
        self.start = new_node
       

    def insert_at_last(self, data):
        # Create a new node
        new_node = Node(data)
        # If the list is empty, new node becomes the head
        if self.start is None:
            self.start = new_node
            return
        # Otherwise, travel to the last node
        current = self.start
        while current.next:
            current = current.next
        # Link the last node to the new node
        current.next = new_node

    def insert_at_position(self, data, position):
        # Position can't be negative
        if position < 0:
            print("Error: Position cannot be negative.")
            return
        # If position is 0, just insert at the front
        if position == 0:
            self.insert_at_first(data)
            return
        # Otherwise, walk through the list until just before the desired position
        current = self.start
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1
        # If we reached None before the desired spot, position is invalid
        if current is None:
            print("Error: Position is out of bounds.")
            return
        # Insert the new node between current and current.next
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def display(self):
        # If list is empty, nothing to show
        if self.start is None:
            print("Linked list is empty.")
            return
        # Otherwise, traverse and print all nodes
        current = self.start
        while current:
            print(current.data, end=" → ")
            current = current.next
        print("None")


# ------------------------------
#  Let's test the insertion operations
# ------------------------------

ll = SLL()

ll.is_empty()

print('\nInserted at first:')
ll.insert_at_first(23)
ll.insert_at_first(53)
ll.insert_at_first(3)
ll.display()

print("\nInserted at last:")
ll.insert_at_last(73)
ll.insert_at_last(55)
ll.display()

print("\nPositional insertion:")
ll.insert_at_position(99, 3)
ll.display()

