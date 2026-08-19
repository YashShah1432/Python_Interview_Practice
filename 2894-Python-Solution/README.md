# LeetCode 2894 - Divisible and Non-divisible Sums Difference

## Problem

Given two positive integers `n` and `m`, calculate:

* The sum of integers from `1` to `n` that are **not divisible by `m`**.
* The sum of integers from `1` to `n` that are **divisible by `m`**.

Return the difference between the two sums.

## Approach

Initialize two variables to store the two sums:

```python
num1 = 0
num2 = 0
```

Iterate from `1` to `n`:

```python
for i in range(1, n+1):
```

If the number is not divisible by `m`, add it to `num1`:

```python
if i % m != 0:
    num1 += i
```

Otherwise, add it to `num2`:

```python
else:
    num2 += i
```

Finally, return the difference:

```python
return num1 - num2
```

## Python Concepts Used

* `for` loop
* `range()`
* Modulo operator `%`
* `if-else` statements
* Variables
* Addition and subtraction
* `return` statement

## Time Complexity

**O(n)**

The loop runs from `1` to `n`.

## Space Complexity

**O(1)**

Only two variables are used to store the sums.

## Key Learning

The key idea is using the **modulo operator `%` to check divisibility**. Numbers with a remainder of `0` are divisible by `m`, while the remaining numbers contribute to the non-divisible sum.
