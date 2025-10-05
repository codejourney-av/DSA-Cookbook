# 🚦 Queue Data Structure in Python

A **Queue** is a linear data structure that follows the **FIFO (First In, First Out)** principle.  
This means the element that is **inserted first** is the one that gets **removed first** — just like people waiting in a queue at a ticket counter.

---

## 🧠 Real-Life Analogy

Think of a queue as a line of people waiting for service:  
- The **first** person in line is served (**removed**) first.  
- New people **join at the rear** (end) of the line.  
- No one can skip ahead — everyone waits their turn!

---

## 🎯 Why Use a Queue?

Queues are used whenever **order of processing matters** and tasks must be handled **sequentially** and **fairly**.

Common applications include:

- 🖨️ **Task Scheduling** – printer jobs, CPU process scheduling  
- 🌐 **Network Data Handling** – packets sent/received in order  
- 💬 **Message Queues** – used in systems like Kafka or RabbitMQ  
- 🧮 **Breadth-First Search (BFS)** – in trees and graphs  
- 🕹️ **Simulations** – e.g., customers waiting in line  

---

## ⚙️ Key Operations

| Operation    | Description                                       | Time Complexity | Space Complexity |
|---------------|---------------------------------------------------|-----------------|------------------|
| `enqueue(x)`  | Add element `x` to the **rear** of the queue.    | O(1)            | O(1)             |
| `dequeue()`   | Remove and return the element at the **front**.  | O(1)            | O(1)             |
| `peek()`      | Return the **front** element without removing it.| O(1)            | O(1)             |
| `is_empty()`  | Check whether the queue is empty.                | O(1)            | O(1)             |
| `size()`      | Return the number of elements in the queue.      | O(1)            | O(1)             |

🧩 **Overall Space Complexity:** `O(n)` — for storing *n* elements in the queue.

---

## 🔍 Visual Explanation — Enqueue & Dequeue

    FRONT → [10] → [20] → [30] ← REAR
                ↑           ↑
             Dequeue      Enqueue


- **Enqueue:** Elements are added at the **rear** (right side).  
- **Dequeue:** Elements are removed from the **front** (left side).  
- The **front** always points to the oldest element, and **rear** to the newest.  

---

## 🧭 Summary

| Feature | Description |
|----------|-------------|
| **Type** | Linear Data Structure |
| **Order** | FIFO (First In, First Out) |
| **Primary Operations** | `enqueue()`, `dequeue()`, `peek()` |
| **Common Implementations** | List, Linked List, or `collections.deque` |
| **Use Cases** | Task queues, buffering, BFS, OS scheduling |
| **Overall Time Complexity** | O(1) per operation |
| **Overall Space Complexity** | O(n) |




---

