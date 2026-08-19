# LeetCode 1920 - Build Array from Permutation

## Problem

Given an array `nums` representing a permutation, construct a new array where each element is:

```python
nums[nums[i]]
```

Return the resulting array.

## Approach

Create an empty list to store the result:

```python
ans = []
```

Iterate through every index of `nums`:

```python
for i in range(0, len(nums)):
```

Use `nums[i]` as an index to access another element in `nums`:

```python
ans.append(nums[nums[i]])
```

Finally, return the constructed array.

## Python Concepts Used

* Lists
* `for` loop
* `range()`
* Array indexing
* `append()`
* Nested indexing
* `len()`
* `return` statement

## Time Complexity

**O(n)**

The array is traversed once.

## Space Complexity

**O(n)**

The `ans` list stores `n` elements.

## Key Learning

The key idea is understanding **nested array indexing**:

```python
nums[nums[i]]
```

First, `nums[i]` gives an index, and that index is then used to access another element from `nums`.
