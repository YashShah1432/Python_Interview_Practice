# LeetCode 2176 - Count Equal and Divisible Pairs in an Array

## Problem

Given an integer array `nums` and an integer `k`, count the pairs of indices `(i, j)` where:

* `nums[i] == nums[j]`
* `(i * j) % k == 0`
* `i < j`

## Approach

1. Initialize `count` to `0`.
2. Iterate through all possible pairs of indices using nested loops.
3. Start the second loop from `i + 1` to ensure `i < j`.
4. Check whether the values at both indices are equal.
5. Check whether the product of the indices is divisible by `k`.
6. If both conditions are satisfied, increment `count`.
7. Return the total number of valid pairs.

```python id="bqgqgy"
count = 0
n = len(nums)

for i in range(0, n):
    for j in range(i + 1, n):
        if nums[i] == nums[j] and (i * j) % k == 0:
            count += 1

return count
```

## Python Concepts Used

* **Nested loops** – Generate all possible index pairs.
* **List indexing** – Access elements using their indices.
* **Range** – Start the inner loop from `i + 1` to avoid duplicate pairs.
* **Modulo `%`** – Check divisibility of the index product.
* **Logical `and`** – Verify both conditions simultaneously.
* **Counter variable** – Track the number of valid pairs.

## Time Complexity

**O(n²)** — Every possible pair of indices is checked.

## Space Complexity

**O(1)** — Only a few variables are used as extra space.

## Key Learning

When a problem requires checking **pairs of indices with multiple conditions**, nested loops provide a straightforward brute-force solution, while starting the inner loop from `i + 1` ensures each pair is considered only once.
