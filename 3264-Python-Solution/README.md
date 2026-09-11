# LeetCode 3264 - Final Array State After K Multiplication Operations I

## Problem

Given an array `nums`, perform `k` operations. In each operation, find the **smallest element** in the array and multiply it by `multiplier`. Return the resulting array.

## Approach

1. Repeat the operation `k` times.
2. Find the minimum value using `min(nums)`.
3. Find its index using `nums.index()`.
4. Replace that element with `minimum × multiplier`.
5. Return the modified array.

```python
for i in range(k):
    nums[nums.index(min(nums))] = min(nums) * multiplier
```

The `index()` method ensures that when there are multiple minimum elements, the **first occurrence** is selected.

## Python Concepts Used

* **Lists** – Modify elements directly in the input array.
* **`min()`** – Find the smallest element.
* **`index()`** – Find the position of the first occurrence of the minimum.
* **For loop** – Repeat the operation `k` times.
* **In-place modification** – Update the original list without creating another array.

## Time Complexity

**O(k × n)** — Each operation uses `min()` and `index()`, both taking O(n).

## Space Complexity

**O(1)** — The array is modified in place and no additional data structure is used.

## Key Learning

When an operation must repeatedly modify the **smallest element**, `min()` combined with `index()` provides a simple way to find and update its first occurrence.
