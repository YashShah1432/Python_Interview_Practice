# LeetCode 876 - Middle of the Linked List

## Problem

Given the head of a singly linked list, return the **middle node** of the linked list.

If there are two middle nodes, return the **second middle node**.

## Approach

Use the **slow and fast pointer** technique:

```python id="8b4y3q"
slow = head
fast = head
```

Move `slow` one node at a time and `fast` two nodes at a time:

```python id="4y1j8m"
while fast != None and fast.next != None:
    slow = slow.next
    fast = fast.next.next
```

When `fast` reaches the end of the list, `slow` will be pointing to the middle node.

Finally, return `slow`:

```python id="g7q1rs"
return slow
```

## Python Concepts Used

* Linked lists
* Objects and references
* `while` loop
* Conditional statements
* `.next` pointer
* Multiple variable assignment
* `return` statement

## Time Complexity

**O(n)**

The fast pointer traverses the linked list.

## Space Complexity

**O(1)**

Only two pointer variables are used.

## Key Learning

The key idea is the **slow and fast pointer technique**. The slow pointer moves one step while the fast pointer moves two steps, making the slow pointer reach the middle when the fast pointer reaches the end.
