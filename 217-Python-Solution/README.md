# LeetCode 217 - Contains Duplicate

## Problem

Given an integer array `nums`, determine whether any value appears **at least twice** in the array.

Return `True` if there is a duplicate element; otherwise, return `False`.

## Approach

Convert the array into a `set` using:

```python
set(nums)
```

A set only stores **unique values**.

Therefore:

* If `len(nums) == len(set(nums))`, there are no duplicates.
* If the lengths are different, at least one duplicate exists.

Your solution uses this comparison directly:

```python
return False if len(nums) == len(set(nums)) else True
```

## Python Concepts Used

* Lists
* Sets
* `len()`
* `set()`
* Conditional expression
* `return` statement

## Time Complexity

**O(n)**

Creating a set from the array takes O(n) average time.

## Space Complexity

**O(n)**

The set can contain up to `n` unique elements.

## Key Learning

The key idea is that a **set automatically removes duplicate values**. Comparing the length of the original list with the length of the set provides a simple way to detect whether duplicates exist.
