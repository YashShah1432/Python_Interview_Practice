# LeetCode 78 - Subsets

## Problem

Given an integer array `nums` containing unique elements, return all possible subsets (the power set), including the empty subset and the original array.

## Approach

1. Initialize an empty list `subsets` to store all subsets.
2. Iterate from `0` to `len(nums)` to represent every possible subset size.
3. Use `combinations(nums, i)` to generate all combinations containing exactly `i` elements.
4. Convert each combination into a list and append it to `subsets`.
5. Return the complete list of subsets.

```
subsets = []for i in range(len(nums) + 1):    for combo in combinations(nums, i):        subsets.append(list(combo))return subsets
```

## Python Concepts Used

- Lists and nested lists
- `for` loops
- `range()` and `len()`
- `combinations()` from the `itertools` module
- Type conversion using `list()`
- `append()`

## Time Complexity

O(n × 2ⁿ), where `n` is the length of `nums`, because there are \\(2^n\\) subsets and each subset takes up to O(n) time to construct.

## Space Complexity

O(n × 2ⁿ) to store all subsets, including their elements.

## Key Learning

The `combinations()` function generates selections of a specific size without considering different element orders. Iterating through every subset size from `0` to `n` generates the complete power set, including the empty subset.
