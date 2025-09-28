# 🥞 Stack Data Structure in Python

A **Stack** is a linear data structure that follows the **LIFO (Last In, First Out)** principle.  
Think of it like a stack of plates: the **last plate placed on top** is the **first one removed**.  

---

## 📌 Applications of Stack
- Undo/Redo functionality in text editors  
- Browser history navigation  
- Expression evaluation (infix → postfix/prefix)  
- Function call management (call stack in programming)  

---

## ⚡ Key Operations

| Operation     | Description                                    | Time Complexity |
|---------------|-----------------------------------------------|-----------------|
| `push(x)`     | Insert an element `x` at the top of the stack | **O(1)** |
| `pop()`       | Remove and return the top element             | **O(1)** |
| `peek()`      | Return the top element without removing it    | **O(1)** |
| `is_empty()`  | Check if the stack is empty                   | **O(1)** |
| `size()`      | Return the number of elements in the stack    | **O(1)** |

---

## 🛠️ Example (Stack using Python List)

```python
class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)   # Insert at top

    def pop(self):
        if self.is_empty():
            return "Stack Underflow"
        return self.items.pop()   # Remove from top

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Current stack:", stack.items)
    
    print("Top element (peek):", stack.peek())
    print("Popped:", stack.pop())
    print("Stack after pop:", stack.items)




📂  Implementations in this Repository

This folder contains multiple approaches to implement a stack:

stack_list.py
 → Basic stack using Python list

stack_list_extend.py
 → Stack using list methods (extend, etc.)

stack_sll.py
 → Stack using Singly Linked List

stack_sll_inherent.py
 → Linked List stack using Inheritance

