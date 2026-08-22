# LeetCode 3794 - Reverse Prefix

## Problem

Given a string `s` and an integer `k`, reverse the **first `k` characters** of the string while keeping the remaining characters in their original order.

## Approach

Use string slicing to reverse the first `k` characters:

```python
s[k-1::-1]
```

Then concatenate the unchanged part of the string:

```python
s[k:]
```

Combine both parts:

```python
return s[k-1::-1] + s[k:]
```

## Python Concepts Used

* Strings
* String slicing
* Negative step `-1`
* String concatenation `+`
* `return` statement
* Function parameters

## Time Complexity

**O(n)**

The string is processed to create the reversed prefix and remaining part.

## Space Complexity

**O(n)**

New strings are created for the result.

## Key Learning

The key idea is using **Python slicing with a negative step** to reverse a portion of a string:

```python
s[k-1::-1]
```

This reverses the first `k` characters without changing the remaining characters.
