# LeetCode 3162 - Find the Number of Good Pairs I

## Problem

Given two integer arrays `nums1` and `nums2`, and an integer `k`, count the number of pairs `(i, j)` such that `nums1[i]` is divisible by `nums2[j] * k`.

## Approach

1. Initialize `count` to `0`.
2. Use nested loops to check every possible pair of elements from `nums1` and `nums2`.
3. Calculate `nums2[j] * k`.
4. Check if `nums1[i]` is divisible by this value.
5. If the condition is satisfied, increment `count`.
6. Return the total number of valid pairs.

```python
count = 0

for i in range(len(nums1)):
    for j in range(len(nums2)):
        if nums1[i] % (nums2[j] * k) == 0:
            count += 1

return count
```

## Python Concepts Used

* **Nested loops** – Compare every combination of elements.
* **List indexing** – Access elements from both arrays.
* **Modulo `%`** – Check divisibility.
* **Arithmetic operations** – Calculate `nums2[j] * k`.
* **Counter variable** – Count valid pairs.

## Time Complexity

**O(n × m)** — Where `n` is the length of `nums1` and `m` is the length of `nums2`.

## Space Complexity

**O(1)** — Only a counter variable is used as extra space.

## Key Learning

Nested loops provide a simple way to evaluate **every possible pair** when the constraints allow a brute-force approach.
