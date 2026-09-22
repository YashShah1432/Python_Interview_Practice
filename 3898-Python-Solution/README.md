# LeetCode 3898 - Find Degrees of a Matrix

## Problem

Given a 2D matrix, calculate the **degree of each row** by finding the sum of all elements in that row. Return a list containing the degree of every row.

## Approach

1. Iterate through each row of the matrix.
2. Use `sum()` to calculate the sum of each row.
3. Store the row sums in a new list using list comprehension.
4. Return the resulting list.

```python
return [sum(row) for row in matrix]
```

## Python Concepts Used

* **List comprehension** – Create the result list concisely.
* **`sum()`** – Calculate the sum of elements in each row.
* **2D Lists** – Iterate through rows of the matrix.
* **Iteration** – Process each row independently.

## Time Complexity

**O(n × m)** — Where `n` is the number of rows and `m` is the number of elements in each row.

## Space Complexity

**O(n)** — The result list stores one degree value for each row.

## Key Learning

Python's `sum()` combined with **list comprehension** provides a concise way to calculate and collect row-wise values from a 2D matrix.
