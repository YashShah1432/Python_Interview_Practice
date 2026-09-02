# LeetCode 2824 - Count Pairs Whose Sum is Less than Target

## Problem

Given an integer array `nums` and an integer `target`, count the number of pairs of indices `(i, j)` such that:

```text
i < j
```

and:

```text
nums[i] + nums[j] < target
```

## Approach

Use two nested loops to check every possible pair:

```python
for i in range(0, len(nums)):
    for j in range(i+1, len(nums)):
```

Since `j` starts from `i + 1`, only pairs where `i < j` are considered.

Check whether the sum of the two elements is less than `target`:

```python
if i < j and (nums[i] + nums[j] < target):
    count += 1
```

If the condition is satisfied, increase the pair count.

Finally, return the total number of valid pairs.

## Python Concepts Used

* Lists
* Nested `for` loops
* `range()`
* List indexing
* Comparison operators
* Arithmetic operators
* Counter variable
* `return` statement

## Time Complexity

**O(n²)**

Every possible pair of elements is checked.

## Space Complexity

**O(1)**

Only the `count` variable is used.

## Key Learning

The key idea is to **check every unique pair of elements and count the pairs whose sum is less than the target**.
