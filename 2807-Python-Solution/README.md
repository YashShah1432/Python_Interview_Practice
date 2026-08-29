# LeetCode 2807 - Insert Greatest Common Divisors in Linked List

## Problem

Given a singly linked list, insert a new node containing the **GCD of every pair of adjacent nodes** between them.

## Approach

Start with the head of the linked list:

```python
curr = head
```

Handle an empty list or a list with only one node:

```python
if curr == None or curr.next == None:
    return head
```

Define a `gcd()` function using the Euclidean algorithm:

```python
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
```

Calculate the GCD of the current node and the next node:

```python
divisor = gcd(curr.val, curr.next.val)
```

Create a new node and insert it between the two nodes:

```python
new_node = ListNode(divisor)
new_node.next = curr.next
curr.next = new_node
```

Move to the original next node and continue:

```python
curr = new_node.next
```

Finally, return the modified linked list.

## Python Concepts Used

* Linked lists
* Pointers
* Nested functions
* Euclidean algorithm
* `while` loop
* `.val` attribute
* `.next` pointer
* Object creation
* In-place modification
* `None`
* `return` statement

## Time Complexity

**O(n log V)**

Where `n` is the number of nodes and `V` is the maximum node value. The GCD calculation takes logarithmic time.

## Space Complexity

**O(n)**

New nodes are created between the existing nodes.

## Key Learning

The key idea is to **calculate the GCD of each pair of adjacent nodes and insert a new node containing that GCD between them**.
