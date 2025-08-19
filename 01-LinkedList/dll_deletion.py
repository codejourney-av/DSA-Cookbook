# Doubly Linked List implementation with deletion operations

class Node:
    def __init__(self, previous=None, data=None, next_node=None):
        # Each node stores a value (data), 
        # and has links to the previous and next nodes
        self.previous = previous
        self.data = data
        self.next_node = next_node


class Dll:
    def __init__(self, start=None):
        # Start points to the first node of the doubly linked list
        self.start = start

    def insert_at_last(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data=data)
        
        # Case 1: If the list is empty, new node becomes the first node
        if self.start is None:
            self.start = new_node
            return
        
        # Case 2: Traverse to the last node
        current = self.start
        while current.next_node is not None:
            current = current.next_node
        
        # Attach new node at the end
        current.next_node = new_node
        new_node.previous = current

    def delete_at_first(self):
        """Delete the first node of the list."""
        if self.start is None:
            print("Error: The list is empty.")
            return
        
        # Case 1: Only one node in the list
        if self.start.next_node is None:
            self.start = None
            return
        
        # Case 2: More than one node
        self.start = self.start.next_node
        self.start.previous = None

    def delete_at_last(self):
        """Delete the last node of the list."""
        if self.start is None:
            print("Error: The list is empty.")
            return

        # Case 1: Only one node
        if self.start.next_node is None:
            self.start = None
            return
        
        # Case 2: Traverse to the second-last node
        current = self.start
        while current.next_node.next_node is not None:
            current = current.next_node
        
        # Break the link to the last node
        current.next_node = None

    def delete_at_value(self, value):
        """Delete a node by its value."""
        if self.start is None:
            print("Error: The list is empty.")
            return
        
        # Case 1: First node matches the value
        if self.start.data == value:
            if self.start.next_node:
                self.start = self.start.next_node
                self.start.previous = None
            else:  # Only one node in the list
                self.start = None
            return

        # Case 2: Search for the value in the list
        current = self.start
        while current.next_node is not None:
            if current.next_node.data == value:
                if current.next_node.next_node:
                    # Node to be deleted is in the middle
                    current.next_node.next_node.previous = current
                    current.next_node = current.next_node.next_node
                else:
                    # Node to be deleted is the last node
                    current.next_node = None
                return
            current = current.next_node
            
        print("Error: Value not found.")

    def display(self):
        """Display all nodes in the list."""
        if self.start is None:
            print("Empty list")
            return
        
        current = self.start
        while current is not None:
            print(current.data, end=' <--> ')
            current = current.next_node
        print("None")  # End of the list


# ------------------ Testing the DLL ------------------ #
ll = Dll()

# Insert nodes into DLL
ll.insert_at_last(45)
ll.insert_at_last(55)
ll.insert_at_last(34)
ll.insert_at_last(12)
ll.insert_at_last(58)
ll.insert_at_last(100)
ll.display()
print("-" * 20)

# Delete first node
ll.delete_at_first()
ll.display()
print("-" * 20)

# Delete last node
ll.delete_at_last()
ll.display()
print("-" * 20)

# Delete node by value
ll.delete_at_value(34)
ll.display()
print("-" * 20)
