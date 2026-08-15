# LeetCode 1768 - Merge Strings Alternately

## Problem

Given two strings `word1` and `word2`, merge them by adding their characters alternately, starting with `word1`.

If one string is longer than the other, append the remaining characters at the end.

## Approach

First, find the length of the longer string:

```python
max_length = max(len(word1), len(word2))
```

Then iterate from `0` to `max_length - 1`.

For each index:

* Add the character from `word1` if the index is within its length.
* Add the character from `word2` if the index is within its length.

```python
if i < len(word1):
    merged += word1[i]

if i < len(word2):
    merged += word2[i]
```

This allows the solution to handle strings of different lengths without needing separate loops.

## Python Concepts Used

* Strings
* `len()`
* `max()`
* `for` loop
* `range()`
* String indexing
* Conditional statements
* String concatenation
* `return` statement

## Time Complexity

**O(n + m)**

Where `n` and `m` are the lengths of `word1` and `word2`.

## Space Complexity

**O(n + m)**

The `merged` string contains all characters from both input strings.

## Key Learning

The key idea is to use the **maximum length of the two strings** and conditionally add characters from each string. This handles unequal string lengths while maintaining the required alternating order.
