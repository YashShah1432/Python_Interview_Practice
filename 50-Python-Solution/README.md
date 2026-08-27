# LeetCode 50 - Pow(x, n)

## Problem

Given a floating-point number `x` and an integer `n`, calculate:

```text
x^n
```

Return the result.

## Approach

Use Python's exponentiation operator `**` to directly calculate the power:

```python
return x ** n
```

This handles both positive and negative values of `n`.

## Python Concepts Used

* Function parameters
* Exponentiation operator `**`
* Floating-point numbers
* Integers
* `return` statement

## Time Complexity

**O(log n)**

Python's exponentiation uses an efficient exponentiation algorithm.

## Space Complexity

**O(1)**

No additional data structures are used.

## Key Learning

The key idea is using Python's **`**` exponentiation operator** to calculate the power of a number directly.
