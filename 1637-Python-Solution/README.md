# LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points

## Problem

Given a set of 2D points, find the **maximum width of a vertical area** that contains no points. The width is determined by the largest difference between the x-coordinates of two consecutive points after sorting them.

## Approach

1. Extract all **x-coordinates** from the given points into a separate list.
2. Sort the x-coordinates.
3. Compare every pair of consecutive x-coordinates.
4. Calculate their difference and keep track of the maximum difference.
5. Return the maximum distance found.

```python
arr = []
for i in range(len(points)):
    arr.append(points[i][0])

arr.sort()
```

After sorting, calculate the maximum gap:

```python
for i in range(len(arr)-1):
    if max_dist < arr[i+1] - arr[i]:
        max_dist = arr[i+1] - arr[i]
```

## Python Concepts Used

* **Lists** – Store extracted x-coordinates.
* **List indexing** – Access the x-coordinate using `points[i][0]`.
* **Sorting** – Use `sort()` to arrange coordinates.
* **Loops** – Iterate through points and consecutive coordinates.
* **`float('-inf')`** – Initialize the maximum distance to a very small value.

## Time Complexity

**O(n log n)** — Sorting the x-coordinates takes O(n log n), while scanning them takes O(n).

## Space Complexity

**O(n)** — The separate list stores all x-coordinates.

## Key Learning

For problems involving the **largest gap between values**, sorting the relevant values first allows us to find the maximum gap by checking only **consecutive elements**.
