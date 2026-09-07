# LeetCode 2396 - Strictly Palindromic Number

## Problem

Given an integer `n`, determine whether `n` is **strictly palindromic**.

A number is strictly palindromic if its representation is a palindrome in every base `b` where:

```text
2 <= b <= n - 2
```

## Approach

Check every possible base from `2` to `n - 2`:

```python
for base in range(2, n - 1):
```

For each base, convert `n` into its representation by repeatedly taking the remainder:

```python
digits.append(num % base)
num //= base
```

The resulting digits are stored in reverse order. Compare them with their reversed version:

```python
if digits != digits[::-1]:
    return False
```

If any base does not produce a palindrome, return `False`. Otherwise, return `True`.

## Python Concepts Used

* `for` loop
* `while` loop
* Lists
* List slicing
* `[::-1]`
* Modulo operator `%`
* Integer division `//`
* Conditional statements
* `append()`
* `return` statement

## Time Complexity

**O(n log n)**

The number is converted into multiple bases, with each conversion taking logarithmic time.

## Space Complexity

**O(log n)**

The `digits` list stores the representation of `n` in the current base.

## Key Learning

The key idea is to **convert the number into each required base using repeated division and remainders, then check whether the resulting digit sequence is a palindrome**.
