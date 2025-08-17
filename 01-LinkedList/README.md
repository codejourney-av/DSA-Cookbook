

---

# 🔗 01: Linked Lists

A **Linked List** is a fundamental **linear data structure** where elements (called **nodes**) are connected using **pointers** instead of being stored in **contiguous memory** (like arrays).

Each **node** has two parts:

1. **Data** → The value the node holds (can be a number, string, object, etc.).
2. **Pointer (Link)** → The address/reference to the next node in the sequence.

The **first node** is called the **Head**, and the **last node** points to `None` (or `null`) to indicate the end of the list.

Think of it like a **treasure hunt**:

* Each clue (node) contains information (data)
* Plus a hint about where to find the next clue (pointer).

---

## 📍 Visual Representation

```
[ Data | Next ] -> [ Data | Next ] -> [ Data | Next ] -> None
```

Example:

```
[ 10 | ● ] -> [ 20 | ● ] -> [ 30 | ● ] -> None
```

---

## 🧠 Core Concepts

* **Node** → The building block of a linked list; holds data and a reference to the next node.
* **Head** → The starting point of the list; without it, the list is lost.
* **Tail** → The last node in the list; its pointer is `None`.
* **Traversal** → Visiting each node in sequence from head to tail by following pointers.

---

## ⚡ Time Complexity (Big O)

| Operation              | Average Case | Why?                                                                   |
| ---------------------- | ------------ | ---------------------------------------------------------------------- |
| **Access / Search**    | `O(n)`       | Must start from `HEAD` and follow pointers until the element is found. |
| **Insertion at Head**  | `O(1)`       | Just point the new node to the old head and update `HEAD`.             |
| **Insertion at Tail**  | `O(n)`       | Must traverse the list to find the tail before adding.                 |
| **Deletion at Head**   | `O(1)`       | Just move the `HEAD` to the next node.                                 |
| **Deletion in Middle** | `O(n)`       | Must first find the node before deleting.                              |

---

## ✅ Pros & ❌ Cons

### ✅ Advantages

* **Dynamic Size** → Can grow/shrink without resizing like arrays.
* **Efficient Insertions/Deletions** → Especially at the beginning.

### ❌ Disadvantages

* **No Random Access** → Must traverse from the head every time you want to reach a node.
* **Extra Memory Usage** → Each node stores a pointer in addition to the data.
* **Sequential Access Only** → Can’t jump directly to the middle.

---

## 📌 Types of Linked Lists

1. **Singly Linked List** → Each node points only to the next node.
2. **Doubly Linked List** → Each node has two pointers (next and previous).
3. **Circular Linked List** → Last node points back to the head instead of `None`.

---




