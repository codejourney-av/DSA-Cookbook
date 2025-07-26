# Node class represents an element of the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data      # Value of the node
        self.next = next      # Pointer to the next node

# Singly Linked List class
class SLL:
    def __init__(self, start=None):
        self.start = start    # Start of the linked list

    # Insert a node at the beginning
    def insert_at_first(self, data):
        new_node = Node(data)
        new_node.next = self.start
        self.start = new_node

    # Delete the first node
    def delete_at_first(self):
        if self.start is None:
            print('List is empty')
            return
        self.start = self.start.next  # Move head to next node

    # Delete the last node
    def delete_at_last(self):
        if self.start is None:
            print('List is empty')
            return
        if self.start.next is None:
            self.start = None  # Only one element in the list
            return
        current = self.start
        while current.next.next is not None:
            current = current.next
        current.next = None  # Remove the last node

    # Delete a node with specific value
    def delete_at_item(self, value):
        if self.start is None:
            print('List is empty')
            return
        if self.start.data == value:
            self.start = self.start.next  # If the value is at the first node
            return
        current = self.start
        while current.next is not None:
            if current.next.data == value:
                current.next = current.next.next  # Bypass the node with target value
                return
            current = current.next

    # Display the linked list
    def display(self):
        if self.start is None:
            print('List is empty. Nothing to display.')
            return
        current = self.start
        while current:
            print(current.data, end='  ')
            current = current.next
        print('None')  # Show end of the list

# Testing the linked list
ll = SLL()
ll.insert_at_first(45)
ll.insert_at_first(66)
ll.insert_at_first(68)
ll.insert_at_first(76)


print('Original list:')
ll.display()

print('\nDeleting the first item:')
ll.delete_at_first()
ll.display()

print('\nDeleting the last item:')
ll.delete_at_last()
ll.display()

print('\nDeleting a specific item (76):')
ll.delete_at_item(76)
ll.display()

