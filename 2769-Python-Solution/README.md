# LeetCode 2769 - Find the Maximum Achievable Number

## Problem

Given two integers `num` and `t`, find the maximum achievable value of `x` after performing the allowed operations.

The maximum value can be calculated as:

```text
num + 2 × t
```

## Approach

Each operation can increase the achievable value by `2`.

Therefore, for `t` operations, the total increase is:

```python
t * 2
```

Add this to `num`:

```python
return num + t * 2
```

## Python Concepts Used

* Function parameters
* Multiplication
* Addition
* `return` statement

## Time Complexity

**O(1)**

Only a single calculation is performed.

## Space Complexity

**O(1)**

No additional data structures are used.

## Key Learning

The key idea is recognizing that each operation contributes **2** to the maximum achievable value, so the answer can be calculated directly as `num + 2 * t`.
