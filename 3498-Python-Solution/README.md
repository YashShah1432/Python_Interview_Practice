# LeetCode 3498 - Reverse Degree of a String

## Problem

Given a string `s`, calculate its **reverse degree** by multiplying the reverse alphabetical value of each character by its 1-based position and adding all the results.

## Approach

Calculate the reverse alphabetical value of each character using:

```python
ord('z') - ord(s[i]) + 1
```

Multiply it by the character's 1-based position:

```python
(ord('z') - ord(s[i]) + 1) * (i + 1)
```

Add each value to `reverse_index`:

```python
reverse_index += (ord('z') - ord(s[i]) + 1) * (i + 1)
```

Finally, return the total reverse degree.

## Python Concepts Used

* Strings
* `for` loop
* `range()`
* String indexing
* `ord()`
* Arithmetic operations
* Variables
* `return` statement

## Time Complexity

**O(n)**

The string is traversed once.

## Space Complexity

**O(1)**

Only one variable is used to store the result.

## Key Learning

The key idea is to calculate the **reverse alphabetical value** of each character using `ord()` and multiply it by its **1-based position** in the string.
