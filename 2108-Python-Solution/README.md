# LeetCode 2108 - Find First Palindromic String in the Array

## Problem

Given an array of strings `words`, return the first palindromic string in the array. A palindrome is a string that reads the same forward and backward. If no palindrome exists, return an empty string.

## Approach

1. Iterate through each word in `words`.
2. Reverse the current word using `word[::-1]`.
3. Compare the original word with its reversed version.
4. If both are equal, return the word immediately.
5. If no palindrome is found after checking all words, return an empty string `""`.

```
for word in words:    if word == word[::-1]:        return wordreturn ""
```

## Python Concepts Used

- Lists and string iteration
- `for` loops
- String slicing (`[::-1]`) for reversing a string
- Conditional statements
- Early return
- Empty strings

## Time Complexity

O(n × m), where `n` is the number of words and `m` is the maximum length of a word, because each word may need to be reversed and compared.

## Space Complexity

O(m) for creating a reversed copy of a word.

## Key Learning

Python's `[::-1]` slicing reverses a string. Comparing a string with its reversed version provides a simple way to check whether it is a palindrome. Returning immediately when a match is found ensures that the first palindrome is returned.
