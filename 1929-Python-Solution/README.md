# LeetCode 1929 - Concatenation of Array

## Problem
Given an integer array `nums`, create a new array `ans` that contains `nums` **twice consecutively**.

For example:

```text
nums = [1, 2, 1]

ans = [1, 2, 1, 1, 2, 1]
```

## Approach
Python allows lists to be multiplied by an integer.

```python
nums * 2
```

means:

```text
[1, 2, 3] * 2
```

becomes:

```text
[1, 2, 3, 1, 2, 3]
```

So we simply multiply `nums` by `2` and return the result.

### Example

```python
nums = [1, 2, 1]

ans = nums * 2
```

Output:

```text
[1, 2, 1, 1, 2, 1]
```

## Python Concepts Used
- Lists
- List multiplication
- Assignment
- `return`

## Time Complexity
**O(n)**

The resulting array contains `2n` elements.

## Space Complexity
**O(n)**

A new array containing `2n` elements is created.
