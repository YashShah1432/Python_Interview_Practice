# LeetCode 234 - Palindrome Linked List

## Problem

Given the head of a singly linked list, determine whether the linked list is a **palindrome**.

A palindrome reads the same forward and backward.

## Approach

Use the **slow and fast pointer** technique to find the middle of the linked list:

```python id="r9w4jp"
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
```

Reverse the second half of the linked list using three pointers:

```python id="t7k2qm"
curr = slow
prev = None
nxt = None
```

Reverse the links while traversing:

```python id="x6q3nr"
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
```

Compare the first half with the reversed second half:

```python id="m2v8ks"
while second_half:
    if first_half.val != second_half.val:
        return False
    first_half = first_half.next
    second_half = second_half.next
```

If all corresponding values match, return `True`.

## Python Concepts Used

* Linked lists
* Slow and fast pointers
* Pointers
* `while` loop
* `.val` attribute
* `.next` pointer
* In-place linked list reversal
* Conditional statements
* `None`
* `return` statement

## Time Complexity

**O(n)**

The linked list is traversed a constant number of times.

## Space Complexity

**O(1)**

Only pointer variables are used; no additional data structures are required.

## Key Learning

The key idea is to **find the middle using slow and fast pointers, reverse the second half, and compare it with the first half** to determine whether the linked list is a palindrome.
