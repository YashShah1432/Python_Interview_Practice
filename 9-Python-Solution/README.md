# LeetCode 9 - Palindrome Number

## Problem

Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.

A palindrome number reads the same forward and backward.

## Approach

1. Convert the integer into a string.
2. Reverse the string using Python slicing (`[::-1]`).
3. Compare the original string with the reversed string.
4. If both strings are equal, return `True`; otherwise, return `False`.

## Python Concepts Used

* String Conversion (`str()`)
* String Slicing (`[::-1]`)
* Comparison Operator (`==`)

## Time Complexity

**O(n)**

* Converting the integer to a string takes linear time.
* Reversing the string also takes linear time.

## Space Complexity

**O(n)**

* Additional space is required to store the string representation and its reversed copy.
