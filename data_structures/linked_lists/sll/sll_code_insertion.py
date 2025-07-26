# insertion in linked list
class Node:
    def __init__(self, data= None, next= None):
        self.data = data
        self.next = next
    
class SLL:
    def __init__(self, start= None):
        self.start = start

        
    def is_empty(self):
        if self.start is None:
            print('Linked list is empty, please enter values.')
            return True
        retun False
        
        
    def insert_at_first(self, data):
            new_node= Node(data) 
            new_node.next = self.start # we are assiging the new node link to start
            self.start = new_node # we are assinging the recently added number as new node
             # like this ((new_node ➡️ 53 ➡️ 23 ➡️ None))
             # final look will be : start ➡️ 53 ➡️ 23 ➡️ None

            
            
            
    def insert_at_last(self,data):
        new_node = Node(data)
        if self.start is None:
            self.start = new_node
            return
        else:
            current = self.start
            while  current.next:
                current = current.next
            current.next = new_node
                 
            
    def insert_at_position(self, data, position):
        #Is the position value valid? It can't be negative.
        if position < 0:
            print("Error: Position cannot be negative.")
            return
        #Is the position 0? If so, use our existing function.
        if position == 0:
            self.insert_at_first(data)
            return
        else:
            current = self.start     # 'current' is the person we're currently looking at in the line.
            count = 0     # 'count' is the position of the 'current' person.
             # We walk the line until we find the person at 'position - 1'.
             # We also stop if 'current' is None, which means we hit the end of the line.
            while current and count < position -1:
                current = current.next
                count += 1
            # After the loop, we must check if we fell off the end of the list.
           # If 'current' is None, the position was too large (e.g., asking for spot 10 in a line of 3).
            if current is None:
                print("Error: Position is out of bounds.")
                return         
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node        
        
     
        
    
    def display(self):
        if self.start is None:
            print("LL is empty.")
            return
        else:
            current = self.start
            while current :
                print(current.data, end='-> ')
                current = current.next
            print("None")
        
    
ll = SLL()
ll.is_empty()

print('inserted at first')
ll.insert_at_first(23)
ll.insert_at_first(53)
ll.insert_at_first(3)
ll.display()

print("inserted at last")
ll.insert_at_last(73)
ll.insert_at_last(55)
ll.display()

print("positional insertion")
ll.insert_at_position(99,3)
ll.display()

