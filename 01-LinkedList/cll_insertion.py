class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = self  # Each new node points to itself


class Cll:
    def __init__(self, last=None):
        self.last = last

    # Insert at the beginning
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node

    # Insert at the end
    def insert_at_last(self, data):
        if self.last is None:
            self.insert_at_first(data)
        else:
            new_node = Node(data)
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node

    # Insert after a specific position (0-based index)
    def insert_at_position(self, data, position):
        if position < 0:
            print("Error: position out of bound.")
            return

        if self.last is None or position == 0:
            self.insert_at_first(data)
            return

        new_node = Node(data)
        current = self.last.next
        count = 0

        while current != self.last and count < position - 1:
            current = current.next
            count += 1

        if count != position - 1:
            print("Error: position does not exist.")
            return

        new_node.next = current.next
        current.next = new_node

        if current == self.last:
            self.last = new_node

    # Search for a value in the list
    def search(self, data):
        if self.last is None:
            print("Error: list is empty.")
            return None

        current = self.last.next
        while True:
            if current.data == data:
                return current.data
            current = current.next
            if current == self.last.next:
                break
        return None

    # Display the circular list
    def display(self):
        if self.last is None:
            print("List is empty")
            return

        current = self.last.next
        while current != self.last:
            print(current.data, end=" -> ")
            current = current.next
        print(current.data, end=" -> ")
        print("(back to start)")


# Example usage
if __name__ == "__main__":
    cll = Cll()

    print("\nInsert at first:")
    cll.insert_at_first(60)
    cll.insert_at_first(10)
    cll.display()

    print("\nInsert at last:")
    cll.insert_at_last(80)
    cll.insert_at_last(90)
    cll.display()

    print("\nInsert after specific position:")
    cll.insert_at_position(100, 2)
    cll.display()

    print("\nSearch specific value:")
    if cll.search(1):
        print("Search found")
    else:
        print("Search not found")
    cll.display()


### Visualization
10 -> 60 -> 100 -> 80 -> 90 -> (back to start)
