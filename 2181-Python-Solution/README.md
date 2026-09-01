# LeetCode 2181 - Merge Nodes in Between Zeros

## Problem

Given a linked list containing groups of positive integers separated by `0`, merge each group by calculating its **sum** and create a new linked list containing these sums.

## Approach

Start from the node after the first zero:

```python
p1 = head.next
p2 = head.next
```

Create a dummy node to build the result list:

```python
dummy = ListNode(0)
tail = dummy
```

Traverse the list and calculate the sum of values until a `0` is encountered:

```python
while p2 and p2.val != 0:
    total += p2.val
    p2 = p2.next
```

Create a new node containing the calculated sum and add it to the result:

```python
new_node = ListNode(total)
tail.next = new_node
tail = new_node
```

After reaching `0`, move to the beginning of the next group:

```python
if p2:
    p2 = p2.next
    p1 = p2
```

Finally, return the result list:

```python
return dummy.next
```

## Python Concepts Used

* Linked lists
* Pointers
* Nested `while` loops
* `.val` attribute
* `.next` pointer
* Dummy node
* Object creation
* Accumulator variable
* `None`
* `return` statement

## Time Complexity

**O(n)**

Each node is visited once.

## Space Complexity

**O(n)**

A new linked list is created to store the sums.

## Key Learning

The key idea is to **traverse each group of nodes between zeros, calculate its sum, and create a new node containing that sum**.
