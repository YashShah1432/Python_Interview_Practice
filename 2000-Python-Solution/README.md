# LeetCode 2000 - Reverse Prefix of Word

## Problem

Given a string `word` and a character `ch`, reverse the prefix of `word` ending at the **first occurrence** of `ch`. If `ch` does not exist in the string, return the original word.

## Approach

1. Find the first occurrence of `ch` using `find()`.
2. If the character is not found, return the original string.
3. Use slicing with a step of `-1` to reverse the prefix ending at `ch`.
4. Append the remaining part of the string unchanged.

```python
idx = word.find(ch)

if idx == -1:
    return word

return word[idx::-1] + word[idx+1::]
```

## Python Concepts Used

* **`find()`** – Finds the index of the first occurrence of a character.
* **String slicing** – Extracts specific portions of the string.
* **Negative step `-1`** – Reverses the selected substring.
* **String concatenation** – Combines the reversed prefix with the remaining string.
* **Conditional statement** – Handles the case when `ch` is not present.

## Time Complexity

**O(n)** — Finding the character and creating the resulting string take linear time.

## Space Complexity

**O(n)** — String slicing and concatenation create a new string.

## Key Learning

Python string slicing with a **negative step** provides a simple way to reverse a portion of a string without explicitly using a loop.
