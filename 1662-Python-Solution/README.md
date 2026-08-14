# LeetCode 1662 - Check If Two String Arrays are Equivalent

## Problem

Given two string arrays `word1` and `word2`, return `True` if both arrays represent the same string after concatenating all their elements. Otherwise, return `False`.

## Approach

Use `"".join()` to concatenate all strings in each array and then compare the resulting strings.

```python
"".join(word1) == "".join(word2)
```

If both concatenated strings are equal, return `True`; otherwise, return `False`.

## Python Concepts Used

* Lists
* Strings
* `join()` method
* String comparison
* Conditional expression
* `return` statement

## Time Complexity

**O(n + m)**

Where `n` and `m` represent the total number of characters in `word1` and `word2`.

## Space Complexity

**O(n + m)**

New strings are created when joining the elements of both arrays.

## Key Learning

The key idea is that multiple strings in an array can be combined into one string using **`join()`**, after which the two resulting strings can be directly compared.
