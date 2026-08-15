# LeetCode 349 - Intersection of Two Arrays

## Problem

Given two integer arrays `nums1` and `nums2`, return their **intersection**.

Each element in the result must be **unique**, regardless of how many times it appears in the input arrays.

## Approach

Convert both arrays into sets to remove duplicate values:

```python
set(nums1)
set(nums2)
```

Then use the set intersection operator `&` to find the values present in both sets:

```python
set(nums1) & set(nums2)
```

Finally, convert the resulting set back into a list:

```python
list(set(nums1) & set(nums2))
```

## Python Concepts Used

* Sets
* `set()`
* Set intersection operator `&`
* `list()`
* `return` statement

## Time Complexity

**O(n + m)**

Where `n` and `m` are the lengths of `nums1` and `nums2`.

## Space Complexity

**O(n + m)**

Sets are created from both input arrays.

## Key Learning

The key idea is using **sets to remove duplicates** and the set intersection operator `&` to efficiently find common elements between two arrays.
