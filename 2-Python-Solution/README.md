# LeetCode 2 - Add Two Numbers

## Problem

Given two non-empty linked lists representing two non-negative integers, add the two numbers and return the sum as a linked list.

The digits are stored in **reverse order**, and each node contains a single digit.

## Approach

Use two pointers to traverse both linked lists and a variable `c` to store the carry:

```python
curr1 = l1
curr2 = l2
c = 0
```

Create a dummy node to build the answer list:

```python
ans = ListNode(-1)
curr3 = ans
```

Traverse both lists while at least one list still has nodes:

```python
while curr1 or curr2:
```

Add the current digits and the carry:

```python
total = c
if curr1:
    total += curr1.val
    curr1 = curr1.next
if curr2:
    total += curr2.val
    curr2 = curr2.next
```

If the sum is greater than `9`, store the carry and keep the single digit:

```python
if total > 9:
    c = 1
    total -= 10
```

Create a new node with the calculated digit and add it to the result list.

After the loop, if a carry remains, add it as the final node.

## Python Concepts Used

* Linked lists
* Two pointers
* `while` loop
* Conditional statements
* `.val` attribute
* `.next` pointer
* Carry handling
* Object creation
* In-place linked list construction
* `None`
* `return` statement

## Time Complexity

**O(max(n, m))**

Both linked lists are traversed once.

## Space Complexity

**O(max(n, m))**

The result linked list requires space for the sum.

## Key Learning

The key idea is to **traverse both linked lists digit by digit, add the values along with the carry, and create a new linked list containing the resulting digits**.
