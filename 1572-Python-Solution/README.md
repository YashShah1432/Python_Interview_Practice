# LeetCode 1572 - Matrix Diagonal Sum

## Problem

Given a square matrix `mat`, calculate the sum of the elements on both the **primary diagonal** and the **secondary diagonal**.

If the matrix has an odd number of rows, the center element belongs to both diagonals, so it should be counted only once.

## Approach

First, traverse the matrix and collect the elements where the row and column indexes are equal:

```python
if i == j:
    result.append(mat[i][j])
```

These elements belong to the **primary diagonal**.

Then traverse the matrix from the right side and collect the elements belonging to the **secondary diagonal**. The condition:

```python
if i == j:
    break
```

prevents the center element from being counted twice.

Finally, calculate the sum of all collected diagonal elements:

```python
return sum(result)
```

## Python Concepts Used

* Nested `for` loops
* 2D Lists
* Matrix indexing
* `range()`
* Conditional statements
* `break`
* `append()`
* `sum()`

## Time Complexity

**O(n²)**

The matrix is traversed using nested loops.

## Space Complexity

**O(n)**

The `result` list stores the diagonal elements.

## Key Learning

The key idea is identifying diagonal elements using their **row and column indexes**. The primary diagonal satisfies `i == j`, while the secondary diagonal follows the opposite direction. The center element must be counted only once.
