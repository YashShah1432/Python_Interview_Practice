# LeetCode 61 - Rotate List

## Problem

Given the head of a singly linked list and an integer `k`, rotate the linked list to the right by `k` positions.

## Approach

Use two pointers, `p1` and `p2`, along with a pointer to count the length of the linked list:

```python
p1 = head
p2 = head
curr = head
```

Handle an empty list, a single-node list, or `k = 0`:

```python
if p1 == None or p1.next == None or k == 0:
    return head
```

Find the length of the linked list:

```python
while curr:
    curr = curr.next
    count += 1
```

Reduce unnecessary rotations using modulo:

```python
k %= count
```

Move `p1` forward by `k` nodes:

```python
for i in range(k):
    p1 = p1.next
```

Move both pointers until `p1` reaches the last node:

```python
while p1.next:
    p1 = p1.next
    p2 = p2.next
```

Set `p2.next` as the new head and connect the original head after the last node:

```python
new_head = p2.next
p2.next = None
p1.next = head
```

Finally, return the new head.

## Python Concepts Used

* Linked lists
* Two pointers
* `while` loop
* `for` loop
* `.next` pointer
* Modulo operator `%`
* List traversal
* In-place modification
* `None`
* `return` statement

## Time Complexity

**O(n)**

The linked list is traversed a constant number of times.

## Space Complexity

**O(1)**

Only pointer variables are used.

## Key Learning

The key idea is to **find the length, reduce `k` using modulo, position two pointers `k` nodes apart, and reconnect the list at the correct position to rotate it efficiently**.
