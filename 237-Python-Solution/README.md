# LeetCode 237 - Delete Node in a Linked List

## Problem

Given a node in a singly linked list, delete that node from the linked list without having access to the head of the list.

## Approach

Copy the value of the next node into the current node:

```python
node.val = node.next.val
```

Then skip the next node by changing the current node's `next` pointer:

```python
node.next = node.next.next
```

This effectively removes the given node from the linked list.

## Python Concepts Used

* Linked lists
* Objects and references
* `.val` attribute
* `.next` pointer
* In-place modification
* Assignment
* `return` statement

## Time Complexity

**O(1)**

Only the given node and its next node are modified.

## Space Complexity

**O(1)**

No additional data structures are used.

## Key Learning

The key idea is to **copy the next node's value into the current node and then skip the next node**, allowing the given node to be deleted without accessing the head of the linked list.
