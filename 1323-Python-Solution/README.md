# LeetCode 1323 - Maximum 69 Number

## Problem

Given a positive integer containing only the digits `6` and `9`, change at most one digit from `6` to `9` to obtain the maximum possible number.

## Approach

1. Convert the number into a string.
2. Use `replace("6", "9", 1)` to replace only the **first occurrence** of `6` with `9`.
3. Convert the resulting string back into an integer.
4. Return the modified number.

```python
return int(str(num).replace("6", "9", 1))
```

Replacing the first `6` is sufficient because changing the leftmost `6` gives the highest possible increase in the number.

## Python Concepts Used

- `str()` for converting an integer to a string
- `replace()` with a count parameter
- `int()` for converting the result back to an integer
- String manipulation
- One-line return expression

## Time Complexity

**O(n)**, where `n` is the number of digits in `num`.

## Space Complexity

**O(n)** for the string representation of the number.

## Key Learning

The `replace()` method can take a third argument specifying how many occurrences to replace. Using `replace("6", "9", 1)` allows the first `6` to be changed directly without manually iterating through the digits.
