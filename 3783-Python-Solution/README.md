# LeetCode 3783 - Mirror Distance

## Problem

Given an integer `n`, reverse its digits and return the absolute difference between the original number and its reversed number.

## Approach

Create the reversed number by extracting digits from right to left.

Use `% 10` to get the last digit:

```python
r = temp % 10
```

Remove the last digit using integer division:

```python
temp //= 10
```

Build the reversed number:

```python
num = (num * 10) + r
```

Finally, calculate the absolute difference:

```python
return abs(n - num)
```

## Python Concepts Used

* `while` loop
* Modulo operator `%`
* Integer division `//`
* Arithmetic operations
* `abs()`
* Variables
* `return` statement

## Time Complexity

**O(d)**

Where `d` is the number of digits in `n`.

## Space Complexity

**O(1)**

Only a few variables are used regardless of the number of digits.

## Key Learning

The key idea is to **reverse an integer using `% 10` and `// 10`**, then use `abs()` to calculate the distance between the original and reversed numbers.
