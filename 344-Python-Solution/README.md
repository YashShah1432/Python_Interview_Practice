# LeetCode 344 - Reverse String

## Problem

Given a character array `s`, reverse the array **in-place**.

You must modify the input array directly without creating another array.

## Approach

Use the **two-pointer swapping technique**.

Start from the beginning of the array and swap each element with its corresponding element from the end:

```python
s[i], s[len(s) - i - 1] = s[len(s) - i - 1], s[i]
```

The condition:

```python
i < len(s) - i
```

ensures that elements are swapped only until the middle of the array is reached.

For example:

```text
[a, b, c, d, e]
```

The swaps are:

```text
a ↔ e
b ↔ d
```

Result:

```text
[e, d, c, b, a]
```

## Python Concepts Used

* `for` loop
* `range()`
* List indexing
* Multiple assignment
* Tuple unpacking
* In-place modification
* `len()`
* `return` statement

## Time Complexity

**O(n)**

The array is traversed approximately once.

## Space Complexity

**O(1)**

The array is reversed in-place without using an additional array.

## Key Learning

The key idea is **in-place swapping** using two corresponding positions from opposite ends of the array. Multiple assignment in Python allows both values to be swapped in a single statement.
