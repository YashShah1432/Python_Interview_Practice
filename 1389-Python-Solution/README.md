# LeetCode 1389 - Create Target Array in the Given Order

## Problem

Given two arrays `nums` and `index`, create a target array by inserting `nums[i]` at position `index[i]` for each element.

## Approach

1. Initialize an empty `target` list.
2. Iterate through all elements using their indices.
3. Insert `nums[i]` at position `index[i]` using `insert()`.
4. Return the resulting target array.

```python
target = []

for i in range(len(index)):
    target.insert(index[i], nums[i])

return target
```

## Python Concepts Used

* **Lists** – Store the target array.
* **`insert()`** – Insert an element at a specific index.
* **For loop** – Process each element in order.
* **List indexing** – Access corresponding elements from `nums` and `index`.

## Time Complexity

**O(n²)** — Inserting into a Python list can take O(n), and it is performed up to `n` times.

## Space Complexity

**O(n)** — The `target` list stores all `n` elements.

## Key Learning

Python's `list.insert()` makes it simple to build an array when elements need to be placed at **specific positions** while preserving the required insertion order.
