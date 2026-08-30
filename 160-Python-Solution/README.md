# LeetCode 160 - Intersection of Two Linked Lists

## Problem

Given the heads of two singly linked lists, find the node at which the two linked lists **intersect**.

If the linked lists do not intersect, return `None`.

## Approach

Use two pointers and first calculate the lengths of both linked lists:

```python
p1 = headA
p2 = headB
```

Traverse both lists to find their lengths:

```python
while p1:
    p1 = p1.next
    lenA += 1

while p2:
    p2 = p2.next
    lenB += 1
```

Calculate the difference between the two lengths:

```python
diff = abs(lenA - lenB)
```

Move the pointer of the longer list forward by the length difference so both pointers have the same distance from the end:

```python
if lenA > lenB:
    for i in range(diff):
        p1 = p1.next
else:
    for i in range(diff):
        p2 = p2.next
```

Move both pointers together and compare their node references:

```python
while p1:
    if p1 == p2:
        return p1
    p1 = p1.next
    p2 = p2.next
```

If no common node is found, return `None`.

## Python Concepts Used

* Linked lists
* Two pointers
* `while` loop
* `for` loop
* `.next` pointer
* Object/reference comparison
* `abs()`
* Conditional statements
* `None`
* `return` statement

## Time Complexity

**O(n + m)**

Both linked lists are traversed to calculate their lengths and find the intersection.

## Space Complexity

**O(1)**

Only pointer and length variables are used.

## Key Learning

The key idea is to **align both linked lists by their lengths**. Once both pointers have the same distance from the end, moving them together allows us to find the first common node.
