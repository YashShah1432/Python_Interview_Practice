# LeetCode 1266 - Minimum Time Visiting All Points

## Problem

Given a list of points on a 2D plane, find the minimum time required to visit all points in the given order. In one second, you can move one unit horizontally, vertically, or diagonally.

## Approach

1. Initialize `time` to `0`.
2. Iterate through every pair of consecutive points.
3. Calculate the horizontal distance using the absolute difference of their x-coordinates.
4. Calculate the vertical distance using the absolute difference of their y-coordinates.
5. The minimum time between two points is the maximum of these two distances.
6. Add this time to the total and return the result.

```python
time = 0

for i in range(len(points) - 1):
    time += max(
        abs(points[i][0] - points[i + 1][0]),
        abs(points[i][1] - points[i + 1][1])
    )

return time
```

## Python Concepts Used

* **Lists** – Store the coordinates of the points.
* **List indexing** – Access x and y coordinates.
* **`abs()`** – Calculate absolute distance between coordinates.
* **`max()`** – Determine the minimum time required between two points.
* **For loop** – Process consecutive points.
* **Accumulator variable** – Store the total travel time.

## Time Complexity

**O(n)** — Each pair of consecutive points is processed once.

## Space Complexity

**O(1)** — Only the `time` variable and temporary calculations are used.

## Key Learning

When diagonal movement is allowed, the minimum time between two points is determined by the **larger of the horizontal and vertical distances**.
