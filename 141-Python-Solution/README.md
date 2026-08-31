# LeetCode 141 - Linked List Cycle

## Problem

Given the head of a singly linked list, determine whether the linked list contains a **cycle**.

A cycle exists when a node's `next` pointer points back to a previous node in the linked list.

## Approach

Use the **slow and fast pointer** technique:

```python
slow = head
fast = head
```

Handle an empty list or a list with only one node:

```python
if not head or not head.next:
    return False
```

Move `slow` one step and `fast` two steps at a time:

```python
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

If there is a cycle, the two pointers will eventually meet:

```python
if slow == fast:
    return True
```

If `fast` reaches `None`, there is no cycle:

```python
return False
```

## Python Concepts Used

* Linked lists
* Slow and fast pointers
* `while` loop
* `.next` pointer
* Object/reference comparison
* Conditional statements
* `None`
* `return` statement

## Time Complexity

**O(n)**

The pointers traverse the linked list at most a linear number of times.

## Space Complexity

**O(1)**

Only two pointer variables are used.

## Key Learning

The key idea is the **Floyd's Cycle Detection algorithm**, where the slow pointer moves one step and the fast pointer moves two steps. If they meet, a cycle exists.
