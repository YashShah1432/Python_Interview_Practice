# LeetCode 206 - Reverse Linked List

## Problem

Given the head of a singly linked list, reverse the linked list and return the new head.

## Approach

Use three pointers to reverse the links:

```python
curr = head
nxt = None
prev = None
```

Traverse the linked list while `curr` is not `None`:

```python
while curr != None:
```

Store the next node before changing the current node's link:

```python
nxt = curr.next
```

Reverse the current node's pointer:

```python
curr.next = prev
```

Move `prev` and `curr` forward:

```python
prev = curr
curr = nxt
```

When the loop finishes, `prev` points to the new head:

```python
return prev
```

## Python Concepts Used

* Linked lists
* Pointers
* `while` loop
* `.next` pointer
* Variable assignment
* In-place modification
* `None`
* `return` statement

## Time Complexity

**O(n)**

The linked list is traversed once.

## Space Complexity

**O(1)**

Only three pointer variables are used.

## Key Learning

The key idea is to **reverse each node's `next` pointer** using `prev`, `curr`, and `nxt` pointers while traversing the linked list.
