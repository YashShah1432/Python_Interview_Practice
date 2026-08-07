# LeetCode 125 - Valid Palindrome

## Problem
Given a string `s`, determine whether it is a palindrome after:
- Converting all uppercase letters to lowercase.
- Removing all non-alphanumeric characters.

Return `true` if the resulting string is a palindrome; otherwise, return `false`.

## Approach
1. Traverse each character in the input string.
2. Keep only alphanumeric characters using `isalnum()`.
3. Convert all characters to lowercase using `lower()`.
4. Build a cleaned string containing only lowercase letters and digits.
5. Reverse the cleaned string using slicing (`[::-1]`).
6. Compare the cleaned string with its reverse.
7. Return `True` if they are identical; otherwise, return `False`.

## Python Concepts Used
- String Comprehension (Generator Expression)
- `join()`
- `lower()`
- `isalnum()`
- String Slicing (`[::-1]`)
- String Comparison

## Time Complexity
**O(n)**

- Traverse the string once to create the cleaned string.
- Reverse the cleaned string once.

## Space Complexity
**O(n)**

- An additional string is created to store the cleaned characters.
