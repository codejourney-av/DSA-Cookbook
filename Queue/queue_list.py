class Queue:
    def __init__(self):
        self.que_list = []
    
    def is_empty(self):
        return len(self.que_list) == 0
    
    def enqueue(self, data):
        """Add an element to the rear of the queue."""
        self.que_list.append(data)
    
    def dequeue(self):
        """Remove and return the front element of the queue."""
        if not self.is_empty():
            return self.que_list.pop(0)
        else:
            raise IndexError("Queue is empty!")
    
    def get_front(self):
        """Return the front element without removing it."""
        if not self.is_empty():
            return self.que_list[0]
        else:
            raise IndexError("Queue is empty!")
    
    def get_rear(self):
        """Return the rear element without removing it."""
        if not self.is_empty():
            return self.que_list[-1]
        else:
            raise IndexError("Queue is empty!")
        
    def size(self):
        """Return the number of elements in the queue."""
        return len(self.que_list)
    
    def __str__(self):
        """Return a user-friendly representation of the queue."""
        return " <- ".join(map(str, self.que_list))


# Driver code
q = Queue()

try:
    print("Is queue empty?", q.is_empty())
except IndexError as e:
    print(e.args[0])

q.enqueue(33)
q.enqueue(86)
q.enqueue(93)
q.enqueue(6)
q.enqueue(13)
q.enqueue(26)

print("Queue:", q)
print("Front element:", q.get_front())
print("Rear element:", q.get_rear())

try:
    q.dequeue()
    print("Queue after one dequeue:", q)
    print("Queue size now:", q.size(), "elements")
except IndexError as e:
    print(e.args[0])
