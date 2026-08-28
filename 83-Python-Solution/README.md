# LeetCode 83 - Remove Duplicates from Sorted List

## Problem

Given the head of a **sorted singly linked list**, remove all duplicate values so that each value appears only once.

Return the modified linked list.

## Approach

First handle an empty list or a list with only one node:

```python
if head == None or head.next == None:
    return head
```

Use a pointer `curr` to traverse the list:

```python
curr = head
```

Since the list is sorted, duplicate values will be next to each other. Compare the current node with the next node:

```python
if curr.val == curr.next.val:
    curr.next = curr.next.next
```

If the values are different, move to the next node:

```python
else:
    curr = curr.next
```

Continue until the end of the list and return the head.

## Python Concepts Used

* Linked lists
* Pointers
* `while` loop
* Conditional statements
* `.val` attribute
* `.next` pointer
* In-place modification
* `return` statement

## Time Complexity

**O(n)**

The linked list is traversed once.

## Space Complexity

**O(1)**

Only one pointer variable is used.

## Key Learning

The key idea is that because the linked list is **sorted**, duplicate values are adjacent. We can remove duplicates by skipping the next node whenever two consecutive nodes have the same value.
