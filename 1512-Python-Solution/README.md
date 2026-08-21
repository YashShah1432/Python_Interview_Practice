# LeetCode 1512 - Number of Good Pairs

## Problem

Given an integer array `nums`, find the number of **good pairs** `(i, j)` where:

```text
i < j
```

and:

```text
nums[i] == nums[j]
```

## Approach

Use two nested loops to compare every possible pair of elements:

```python
for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
```

Start `j` from `i + 1` to ensure that `i < j`.

If both values are equal, increment `pairs`:

```python
if nums[i] == nums[j]:
    pairs += 1
```

Finally, return the total number of good pairs.

## Python Concepts Used

* Lists
* Nested `for` loops
* `range()`
* List indexing
* Comparison operators
* Counter variables
* `return` statement

## Time Complexity

**O(n²)**

The nested loops compare every possible pair of elements.

## Space Complexity

**O(1)**

Only the `pairs` variable and loop variables are used.

## Key Learning

The key idea is to use **nested loops to generate all pairs** while starting the second loop from `i + 1` to ensure that each pair satisfies `i < j` and is counted only once.
