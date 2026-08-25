# LeetCode 231 - Power of Two

## Problem

Given an integer `n`, determine whether `n` is a **power of two**.

A number is a power of two if it can be represented as:

```text
2^x
```

where `x` is a non-negative integer.

## Approach

First handle values that cannot be powers of two:

```python
if n <= 0:
    return False
```

`1` is `2⁰`, so it is a valid power of two:

```python
if n == 1:
    return True
```

If `n` is odd and greater than `1`, it cannot be a power of two:

```python
if n % 2 != 0:
    return False
```

For an even number, divide it by `2` and recursively check the result:

```python
return self.isPowerOfTwo(n // 2)
```

If the number eventually reaches `1`, it is a power of two.

## Python Concepts Used

* Recursion
* `if` statements
* Modulo operator `%`
* Integer division `//`
* Comparison operators
* `return` statement
* Function parameters

## Time Complexity

**O(log n)**

The value of `n` is divided by `2` at each recursive call.

## Space Complexity

**O(log n)**

The recursive calls create a call stack proportional to `log n`.

## Key Learning

The key idea is that a positive power of two can be **repeatedly divided by `2` until it reaches `1`**. If an odd number greater than `1` is encountered, it cannot be a power of two.
