# LeetCode 19 - Remove Nth Node From End of List

## Problem

Given the head of a singly linked list and an integer `n`, remove the **nth node from the end** of the linked list.

Return the head of the modified linked list.

## Approach

Use two pointers, `p1` and `p2`, starting at the head:

```python
p1 = head
p2 = head
```

Move `p1` forward by `n` nodes:

```python
for i in range(n):
    p1 = p1.next
```

If `p1` reaches `None`, the node to remove is the first node:

```python
if p1 == None:
    return head.next
```

Otherwise, move both pointers until `p1` reaches the last node:

```python
while p1.next != None:
    p1 = p1.next
    p2 = p2.next
```

Now `p2.next` is the node that needs to be removed. Skip it:

```python
p2.next = p2.next.next
```

Finally, return the modified head.

## Python Concepts Used

* Linked lists
* Two pointers
* `for` loop
* `while` loop
* `.next` pointer
* Conditional statements
* In-place modification
* `return` statement

## Time Complexity

**O(n)**

The linked list is traversed at most once.

## Space Complexity

**O(1)**

Only two pointer variables are used.

## Key Learning

The key idea is the **two-pointer technique**. By keeping `p1` `n` nodes ahead of `p2`, when `p1` reaches the end, `p2` is positioned just before the node that needs to be removed.
