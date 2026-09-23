# LeetCode 3427 - Sum of Variable Length Subarrays

## Problem

Given an integer array `nums`, calculate the sum of all variable-length subarrays where each index `i` determines the starting position using `i - nums[i]`. The subarray is bounded within the array.

## Approach

1. Initialize `total` to `0`.
2. Iterate through every index `i`.
3. Calculate the starting index using `max(0, i - nums[i])`.
4. Take the subarray from this starting index to `i + 1`.
5. Calculate its sum and add it to `total`.
6. Return the final sum.

```python id="g6v6xj"
total = 0

for i in range(len(nums)):
    total += sum(nums[max(0, i - nums[i]): i+1])

return total
```

## Python Concepts Used

* **List slicing** – Extract the required subarray.
* **`sum()`** – Calculate the sum of each selected subarray.
* **`max()`** – Ensure the starting index does not become negative.
* **For loop** – Process every index in the array.
* **List indexing** – Access elements based on their positions.

## Time Complexity

**O(n²)** — In the worst case, each iteration can calculate the sum of a subarray containing O(n) elements.

## Space Complexity

**O(n)** — List slicing creates a temporary list containing up to O(n) elements.

## Key Learning

When each element defines a **variable-length subarray**, calculate its valid starting index carefully using `max()` and then use Python's slicing and `sum()` operations to process the required range.
