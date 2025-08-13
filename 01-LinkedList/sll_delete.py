#  Singly Linked List - Deletion Operations

class Node:
    def __init__(self, data=None, next=None):
        # A node holds some data and a link to the next node
        self.data = data
        self.next = next


class SLL:
    def __init__(self, start=None):
        # 'start' always points to the head (first node)
        self.start = start

    def insert_at_first(self, data):
        # Create a new node
        new_node = Node(data)
        # Link the new node to the current head
        new_node.next = self.start
        # Move head to point to the new node
        self.start = new_node

    def delete_at_first(self):
        # If list is empty, nothing to delete
        if self.start is None:
            print('List is empty. Nothing to delete.')
            return
        # Just move head to the second node
        self.start = self.start.next

    def delete_at_last(self):
        # If list is empty
        if self.start is None:
            print('List is empty. Nothing to delete.')
            return
        # If only one element exists, clear it
        if self.start.next is None:
            self.start = None
            return
        # Otherwise, walk to the second-last node
        current = self.start
        while current.next.next is not None:
            current = current.next
        # Remove the link to the last node
        current.next = None

    def delete_at_item(self, value):
        # If list is empty
        if self.start is None:
            print('List is empty.')
            return
        # If the head contains the value, remove it
        if self.start.data == value:
            self.start = self.start.next
            return
        # Otherwise, look for the node whose 'next' contains the value
        current = self.start
        while current.next is not None:
            if current.next.data == value:
                # Skip the node containing the value
                current.next = current.next.next
                return
            current = current.next
        print(f"Value {value} not found in the list.")

    def display(self):
        # If list is empty
        if self.start is None:
            print('List is empty. Nothing to display.')
            return
        # Otherwise, print all nodes
        current = self.start
        while current:
            print(current.data, end=' → ')
            current = current.next
        print('None')


# ------------------------------
# Testing the deletion operations
# ------------------------------

ll = SLL()

# Insert some values first
ll.insert_at_first(45)
ll.insert_at_first(66)
ll.insert_at_first(68)
ll.insert_at_first(76)
ll.insert_at_first(86)
ll.insert_at_first(16)
ll.display()

print('\nDeleting the first item:')
ll.delete_at_first()
ll.display()

print('\nDeleting the last item:')
ll.delete_at_last()
ll.display()

print('\nDeleting a specific value (76):')
ll.delete_at_item(76)
ll.display()
