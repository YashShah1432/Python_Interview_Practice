# LeetCode 807 - Max Increase to Keep City Skyline

## Problem

Given a square grid representing building heights, increase the height of buildings as much as possible without changing the **skyline** when viewed from the four directions. Return the total possible increase in building heights.

## Approach

1. Find the maximum height of each row and store it in `row_max`.
2. Find the maximum height of each column and store it in `col_max`.
3. For every cell, the maximum possible height is:
   `min(row_max[i], col_max[j])`.
4. Calculate the difference between this maximum allowed height and the current height.
5. Add all possible increases to `max_height_increase`.

```python id="j7y0qf"
for i in range(n):
    row_max.append(max(grid[i]))
```

For columns, collect each column's elements and find its maximum:

```python id="4zq3yd"
for j in range(n):
    col_ele.append(grid[j][i])

col_max.append(max(col_ele))
```

Finally, calculate the maximum possible increase for every building:

```python id="d6r1hs"
min_height = min(row_max[i], col_max[j])

if grid[i][j] < min_height:
    max_height_increase += min_height - grid[i][j]
```

## Python Concepts Used

* **2D Lists** – Work with the grid of building heights.
* **`max()`** – Find maximum heights in rows and columns.
* **`min()`** – Determine the maximum allowed height for each building.
* **Nested loops** – Traverse rows, columns, and grid cells.
* **List operations** – Store row and column maximums.

## Time Complexity

**O(n²)** — Finding row and column maximums and traversing the grid each take O(n²).

## Space Complexity

**O(n)** — `row_max`, `col_max`, and the temporary `col_ele` list use linear extra space.

## Key Learning

For grid problems where each cell is constrained by its **row and column maximum**, first calculate those maximums and then determine the allowed value for each cell using the minimum of the two.
