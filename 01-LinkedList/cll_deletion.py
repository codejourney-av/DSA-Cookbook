class Node:
     def __init__(self, data = None, next = None):
            self.data = data
            self.next = next

class Cll :
    def __init__(self, last = None):
        self.last = last
    
    def insert_at_first(self, data):
        new_node = Node(data)
        if self.last is None:
            new_node.next = new_node
            self.last = new_node
        else:
            new_node.next = self.last.next
            self.last.next = new_node  # here the last node is pointing the first node as circular list
    
    def is_empty(self):
        return self.last is None
        
    def delete_at_first(self):
        if self.is_empty():
            print("List is empty. NOthing to delete.")
            return
        if self.last.next == self.last:    # if first node is the last node(single node present) 
            self.last = None
        else:
            self.last.next = self.last.next.next   # multiple node, last node points second node from start
        
          
    def delete_at_last(self):
        if self.is_empty():
            print("List is empty.Nothing to delete.")
            return
        if self.last.next == self.last:
            self.last = None
            return
        current = self.last.next
        while current.next != self.last:
            current = current.next
        current.next = self.last.next   # second last node's next now points to the first node
        self.last = current             # self.last pointer points to the second last node now
        
    def delete_at_value(self, value):
        if self.is_empty():
            print("List is empty. Nothing to delete.")
            return
        if self.last.next == self.last:   # single node 
            if self.last.data ==  value:
                self.last = None
            else:
                print("Value not found.")
            return
        if self.last.next.data == value:       # value is in the first node
            self.delete_at_first()
            return
        current = self.last.next               # value is in the middle node
        while current.next != self.last:
            if current.next.data == value:         # now check for the middle nodes
                current.next = current.next.next   # update the address to next node
                return
            current = current.next
        if self.last.data == value:            # value is in the last node
            self.delete_at_last()
        else:
            print("Value not found.")
            
    def display(self):
        if self.is_empty():
            print("List if empty.")
        current = self.last.next
        while current != self.last:
            print(current.data, end = '->')
            current = current.next
        print(current.data, end = '->')
        print('Back to start')
        
        
cll = Cll()
cll.insert_at_first(10)
cll.insert_at_first(20)
cll.insert_at_first(30)
cll.insert_at_first(40)
cll.display()

print("\nDeleting value 30:")
cll.delete_at_value(30)
cll.display()

print("\nDeleting value 10 (first node):")
cll.delete_at_value(10)
cll.display()

print("\nDeleting value 40 (last node):")
cll.delete_at_value(40)
cll.display()

print("\nTrying to delete value 99 (not in list):")
cll.delete_at_value(99)
cll.display()

