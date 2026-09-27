# LeetCode 1464 - Maximum Product of Two Elements in an Array

## Problem

Given an integer array `nums`, find the maximum value of `(nums[i] - 1) * (nums[j] - 1)` where `i != j`.

## Approach

1. Sort the array in descending order.
2. The two largest elements will produce the maximum product.
3. Subtract `1` from both elements.
4. Multiply them and return the result.

```python
nums.sort(reverse=True)

return (nums[0] - 1) * (nums[1] - 1)
```

## Python Concepts Used

* **Lists** – Store the input elements.
* **`sort()`** – Sort the array in descending order.
* **`reverse=True`** – Arrange elements from largest to smallest.
* **List indexing** – Access the two largest elements.
* **Arithmetic operations** – Calculate the required product.

## Time Complexity

**O(n log n)** — Sorting the array takes O(n log n).

## Space Complexity

**O(1)** — The array is sorted in place and no additional data structure is used.

## Key Learning

When the goal is to maximize a product involving two elements, identifying the **two largest values** is sufficient. Sorting in descending order makes these elements directly accessible.
