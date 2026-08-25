# LeetCode 326 - Power of Three

## Problem

Given an integer `n`, determine whether `n` is a **power of three**.

A number is a power of three if it can be represented as:

```text
3^x
```

where `x` is a non-negative integer.

## Approach

First handle values that cannot be powers of three:

```python
if n <= 0:
    return False
```

`1` is `3⁰`, so it is a valid power of three:

```python
if n == 1:
    return True
```

If `n` is not divisible by `3`, it cannot be a power of three:

```python
if n % 3 != 0:
    return False
```

For a number divisible by `3`, divide it by `3` and recursively check the result:

```python
return self.isPowerOfThree(n // 3)
```

If the number eventually reaches `1`, it is a power of three.

## Python Concepts Used

* Recursion
* `if` statements
* Modulo operator `%`
* Integer division `//`
* Comparison operators
* `return` statement
* Function parameters

## Time Complexity

**O(log₃ n)**

The value of `n` is divided by `3` at each recursive call.

## Space Complexity

**O(log₃ n)**

The recursive calls create a call stack proportional to `log₃ n`.

## Key Learning

The key idea is that a positive power of three can be **repeatedly divided by `3` until it reaches `1`**. If a number is not divisible by `3` during this process, it cannot be a power of three.
