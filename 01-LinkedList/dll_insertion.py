#  Doubly Linked List (DLL) - Insertion + Search

class Node:
    def __init__(self, prev=None, data=None, next=None):
        # Each node has 3 parts:
        # prev -> link to the previous node
        # data -> the actual value
        # next -> link to the next node
        self.prev = prev
        self.data = data
        self.next = next


class DLL:
    def __init__(self, start=None):
        # Head pointer (start) always points to the first node
        self.start = start

    def insert_at_first(self, data):
        # Create a new node
        new_node = Node(prev=None, data=data, next=self.start)

        # If the list is not empty, update the old head's prev pointer
        if self.start is not None:
            self.start.prev = new_node

        # Move start to the new node
        self.start = new_node

    def insert_at_last(self, data):
        new_node = Node(data=data)

        # If list is empty, new node becomes head
        if self.start is None:
            self.start = new_node
            return

        # Otherwise, go to the last node
        current = self.start
        while current.next is not None:
            current = current.next

        # Link the new node at the end
        current.next = new_node
        new_node.prev = current

    def insert_at_position(self, data, position):
        # Handle invalid position
        if position < 0:
            print("Error: Position cannot be negative.")
            return

        # If inserting at the very beginning, reuse the existing method
        if position == 0:
            self.insert_at_first(data)
            return

        # Traverse to the node before the target position
        current = self.start
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        # If we ran out of nodes, position is invalid
        if current is None:
            print("Error: Position out of bounds.")
            return

        # Create the new node
        new_node = Node(data=data)

        # Wire up the new node’s links
        new_node.next = current.next
        new_node.prev = current

        # If not inserting at the very end, update the next node's prev link
        if current.next is not None:
            current.next.prev = new_node

        # Update current’s next to point to new_node
        current.next = new_node

    def search(self, data):
        # Walk through the list to look for data
        current = self.start
        while current is not None:
            if current.data == data:
                print(f"Found: {current.data}")
                return
            current = current.next
        print(f"{data} not found in the list.")

    def display(self):
        if self.start is None:
            print("List is empty.")
            return

        # Forward traversal
        current = self.start
        while current is not None:
            print(current.data, end=" ↔ ")
            current = current.next
        print("None")


# ------------------------------
#  Testing the DLL insertions
# ------------------------------

ll = DLL()
print('Inserting at the beginning:')
ll.insert_at_first(45)
ll.insert_at_first(44)
ll.insert_at_first(12)
ll.insert_at_first(65)
ll.insert_at_first(22)
ll.display()

print('\nInserting at the end:')
ll.insert_at_last(100)
ll.display()

print('\nInserting at a specific position (pos=5):')
ll.insert_at_position(112, 5)
ll.display()

print('\nSearching in the DLL:')
ll.search(112)
ll.display()
