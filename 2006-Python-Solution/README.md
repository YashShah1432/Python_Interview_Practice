# LeetCode 2006 - Count Number of Pairs With Absolute Difference K

## Problem

Given an integer array `nums` and an integer `k`, count the number of pairs of indices `(i, j)` where `i < j` and the absolute difference between `nums[i]` and `nums[j]` is exactly `k`.

## Approach

1. Initialize `pair` to `0`.
2. Use nested loops to generate every possible pair of indices.
3. Start the inner loop from `i + 1` to ensure `i < j`.
4. Calculate the absolute difference between the two values using `abs()`.
5. If the difference equals `k`, increment `pair`.
6. Return the total number of valid pairs.

```python
pair = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if abs(nums[i] - nums[j]) == k:
            pair += 1

return pair
```

## Python Concepts Used

* **Nested loops** – Check every possible pair.
* **List indexing** – Access elements at specific indices.
* **`abs()`** – Calculate the absolute difference.
* **`range()`** – Start the second loop from `i + 1`.
* **Counter variable** – Track the number of valid pairs.

## Time Complexity

**O(n²)** — Every possible pair of elements is checked.

## Space Complexity

**O(1)** — Only the counter variable is used as extra space.

## Key Learning

When a problem asks for pairs satisfying a condition, nested loops can be used to examine every unique pair by starting the inner loop from **`i + 1`**.
