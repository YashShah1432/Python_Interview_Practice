# LeetCode 3285 - Find Indices of Stable Mountains

## Problem

Given an array `height` representing mountain heights and a `threshold`, return the indices of all **stable mountains**. A mountain at index `i` is stable when the height of the previous mountain, `height[i-1]`, is greater than the given threshold.

## Approach

1. Start from index `1` because each mountain needs a previous mountain for comparison.
2. Check if `height[i-1] > threshold`.
3. If the condition is true, add index `i` to the result.
4. Return the list of stable mountain indices.

```python
result = []

for i in range(1, len(height)):
    if height[i-1] > threshold:
        result.append(i)
```

## Python Concepts Used

* **Lists** – Store the indices of stable mountains.
* **List indexing** – Access the previous mountain using `height[i-1]`.
* **For loop** – Traverse the array starting from index `1`.
* **Conditional statements** – Check whether the previous height exceeds the threshold.

## Time Complexity

**O(n)** — The array is traversed once.

## Space Complexity

**O(n)** — The result list can contain up to `n-1` indices.

## Key Learning

When a condition depends on the **previous element**, start the loop from index `1` and compare the current index with `i-1`.
