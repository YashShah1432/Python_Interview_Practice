# LeetCode 3146 - Permutation Difference between Two Strings

## Problem

Given two strings `s` and `t` that are permutations of each other, calculate the **permutation difference** between them.

For each character in `s`, find its position in `t` and add the absolute difference between the two positions.

## Approach

Iterate through each character in `s`:

```python
for i in range(0, len(s)):
```

Use `t.index()` to find the position of the current character in `t`:

```python
t.index(s[i])
```

Calculate the absolute difference between its position in `s` and `t`:

```python
abs(i - t.index(s[i]))
```

Add each difference to `total` and return the final result.

## Python Concepts Used

* Strings
* `for` loop
* `range()`
* String indexing
* `index()` method
* `abs()`
* Arithmetic operations
* `return` statement

## Time Complexity

**O(n²)**

For each character in `s`, `index()` may scan the string `t`.

## Space Complexity

**O(1)**

Only the `total` variable and loop variable are used.

## Key Learning

The key idea is to **find the position of each character in the second string and compare it with its position in the first string** using the absolute difference.
