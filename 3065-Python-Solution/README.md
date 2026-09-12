# LeetCode 3065 - Minimum Operations to Exceed Threshold Value I

## Problem

Given an array `nums` and an integer `k`, find the minimum number of operations needed to make all elements in `nums` greater than or equal to `k`. In each operation, remove the smallest element that is less than `k`.

## Approach

1. Initialize `count` to `0`.
2. While the array contains elements smaller than `k`:

   * Find the minimum element using `min()`.
   * Remove it using `remove()`.
   * Increment the operation count.
3. Stop when the minimum element is at least `k`.
4. Return the total number of operations.

```python
count = 0

while len(nums) and min(nums) < k:
    count += 1
    nums.remove(min(nums))

return count
```

## Python Concepts Used

* **Lists** – Store and modify the array.
* **`min()`** – Find the smallest element.
* **`remove()`** – Remove the first occurrence of the minimum element.
* **While loop** – Continue operations until the condition is satisfied.
* **Comparison operators** – Check whether the minimum value is less than `k`.

## Time Complexity

**O(n²)** — `min()` takes O(n) and `remove()` takes O(n), potentially repeated for up to `n` elements.

## Space Complexity

**O(1)** — No additional data structure is used.

## Key Learning

When repeatedly removing elements based on a condition, we can use Python's built-in `min()` and `remove()` methods to directly modify the list until the required condition is achieved.
