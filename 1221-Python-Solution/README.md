# LeetCode 1221 - Split a String in Balanced Strings

## Problem

Given a string `s` containing only `L` and `R`, split it into the maximum number of balanced substrings.

A balanced string contains an equal number of `L` and `R` characters.

## Approach

Use a `balance` variable to keep track of the difference between `L` and `R`:

```python
balance = 0
```

Increment the balance for `L` and decrement it for `R`:

```python
if char == 'L':
    balance += 1
else:
    balance -= 1
```

Whenever the balance becomes `0`, the current substring contains an equal number of `L` and `R`, so increase the balanced substring count:

```python
if balance == 0:
    balanced_count += 1
```

Finally, return the number of balanced substrings.

## Python Concepts Used

* Strings
* `for` loop
* Conditional statements
* Variables
* Comparison operators
* Increment and decrement
* `return` statement

## Time Complexity

**O(n)**

The string is traversed once.

## Space Complexity

**O(1)**

Only two variables are used.

## Key Learning

The key idea is to **track the balance between `L` and `R`**. Whenever the balance becomes `0`, a balanced substring has been found.
