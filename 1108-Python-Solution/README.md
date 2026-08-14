# LeetCode 1108 - Defanging an IP Address

## Problem

Given a valid IPv4 address `address`, return its **defanged version**.

A defanged IP address replaces every `.` with `[.]`.

## Approach

Use Python's `replace()` method to replace every dot in the IP address with `[.]`.

```python
address.replace('.', '[.]')
```

This directly replaces all occurrences of `.` in the string and returns the modified address.

## Python Concepts Used

* Strings
* `replace()` method
* `return` statement
* Function parameters

## Time Complexity

**O(n)**

The string is traversed to find and replace the dots.

## Space Complexity

**O(n)**

A new string is created with the replaced characters.

## Key Learning

The key idea is using the built-in **`replace()` string method** to efficiently replace all occurrences of a specific character or substring.
