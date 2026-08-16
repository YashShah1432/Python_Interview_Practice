# LeetCode 136 - Single Number

## Problem

Given a non-empty integer array `nums`, every element appears **twice** except for one element that appears exactly once.

Find and return the element that appears only once.

## Approach

Use the **XOR (`^`) operator** to find the unique number.

Initialize `result` to `0`:

```python
result = 0
```

Then XOR every number with `result`:

```python
for num in nums:
    result = result ^ num
```

XOR has two important properties:

* `x ^ x = 0`
* `x ^ 0 = x`

Therefore, all numbers that appear twice cancel each other out, leaving only the number that appears once.

## Python Concepts Used

* `for` loop
* Bitwise XOR operator `^`
* Variables
* Arithmetic/bitwise operations
* `return` statement

## Time Complexity

**O(n)**

The array is traversed exactly once.

## Space Complexity

**O(1)**

Only one additional variable, `result`, is used.

## Key Learning

The key idea is using the **XOR operation** because duplicate numbers cancel each other out:

```text
a ^ a = 0
a ^ 0 = a
```

This allows the single number to be found without using extra data structures.
