# LeetCode 80 - Remove Duplicates from Sorted Array II

## Problem

Given a sorted integer array `nums`, remove duplicates in-place so that each unique element appears at most twice. Return the number of valid elements, `k`, while keeping the relative order of the elements unchanged.

## Approach

1. If the array contains at most two elements, return its length directly.
2. Initialize `write_index = 2`, since the first two elements can always remain.
3. Iterate through the array starting from index `2`.
4. Compare the current element `nums[i]` with `nums[write_index - 2]`.
5. If they are different, place the current element at `nums[write_index]` and increment `write_index`.
6. Return `write_index`, which represents the length of the modified array.

```
if len(nums) <= 2:    return len(nums)write_index = 2for i in range(2, len(nums)):    if nums[i] != nums[write_index - 2]:        nums[write_index] = nums[i]        write_index += 1return write_index
```

## Python Concepts Used

- Lists and indexing
- `len()`
- `for` loops and `range()`
- Conditional statements
- In-place array modification
- Two-pointer technique
- Increment operator (`+=`)

## Time Complexity

O(n), where `n` is the length of `nums`, because the array is traversed once.

## Space Complexity

O(1) because the modification is performed in-place using a constant number of variables.

## Key Learning

The two-pointer technique allows duplicates to be removed in-place without creating another array. Comparing the current element with the element two positions behind the write pointer ensures that each unique value appears at most twice.
