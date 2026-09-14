# LeetCode 836 - Rectangle Overlap

## Problem

Given two axis-aligned rectangles `rec1` and `rec2`, determine whether they overlap with a **positive area**. Rectangles that only touch at an edge or corner are not considered overlapping.

## Approach

1. Calculate the overlapping width using the minimum of the right boundaries and the maximum of the left boundaries.
2. Calculate the overlapping height using the minimum of the top boundaries and the maximum of the bottom boundaries.
3. Use `max(0, ...)` to ensure width and height are not negative.
4. Calculate the overlapping area as `w * h`.
5. If the area is greater than `0`, the rectangles overlap.

```python
w = max(0, min(rec1[2], rec2[2]) - max(rec1[0], rec2[0]))
h = max(0, min(rec1[3], rec2[3]) - max(rec1[1], rec2[1]))

area = w * h

return True if area > 0 else False
```

## Python Concepts Used

* **`min()`** – Find the smaller boundary between the rectangles.
* **`max()`** – Calculate the starting boundary and prevent negative overlap.
* **Arithmetic operations** – Calculate the overlapping width and height.
* **Conditional expression** – Return `True` when the overlapping area is positive.
* **Lists and indexing** – Access rectangle coordinates.

## Time Complexity

**O(1)** — Only a fixed number of calculations are performed.

## Space Complexity

**O(1)** — Only a few variables are used.

## Key Learning

For rectangle overlap problems, calculate the **intersection width and height** first. A positive value for both dimensions means the rectangles have a positive overlapping area.
