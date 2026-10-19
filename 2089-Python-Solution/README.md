# LeetCode 2089 - Find Target Indices After Sorting Array

## Problem

Given an integer array `nums` and an integer `target`, sort the array in non-decreasing order and return all indices where the value equals `target`.

## Approach

1. Sort `nums` in ascending order using `sort()`.
2. Initialize an empty list `result` to store the target indices.
3. Iterate through the sorted array.
4. If the current element is greater than `target`, stop the loop using `break`, since all remaining elements will also be greater.
5. If the current element equals `target`, append its index to `result`.
6. Return the list of target indices.

```
nums.sort()result = []for i in range(len(nums)):    if nums[i] > target:        break    if nums[i] == target:        result.append(i)return result
```

## Python Concepts Used

- Lists and indexing
- `sort()`
- `for` loops
- `range()` and `len()`
- Conditional statements
- `break`
- `append()`

## Time Complexity

O(n log n), where `n` is the length of `nums`, due to sorting. The subsequent traversal takes O(n) time in the worst case.

## Space Complexity

O(n) in the worst case for storing the target indices in `result`. Sorting may also require additional implementation-dependent space.

## Key Learning

Sorting places equal values next to each other, making it easy to collect all their indices. Since the array is sorted, using `break` when an element exceeds `target` avoids checking unnecessary elements.
