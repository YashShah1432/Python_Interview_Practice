# LeetCode 2545 - Sort the Students by Their Kth Score

## Problem

Given a 2D array `score` where each row represents a student's scores, sort the students in **descending order** based on their score in the `k`-th exam.

## Approach

1. Use Python's `sort()` method to sort the `score` list.
2. Use a `lambda` function as the sorting key.
3. Access the `k`-th score using `x[k]`.
4. Set `reverse=True` to sort the scores in descending order.
5. Return the sorted `score` list.

```python id="6k6t7m"
score.sort(key=lambda x: x[k], reverse=True)

return score
```

## Python Concepts Used

* **`sort()`** – Sort the list in place.
* **`lambda` function** – Define the sorting key based on the `k`-th score.
* **List indexing** – Access the score at index `k`.
* **`reverse=True`** – Sort values in descending order.
* **In-place sorting** – Modify the original `score` list directly.

## Time Complexity

**O(m × log m)** — Where `m` is the number of students. Sorting the students takes O(m log m).

## Space Complexity

**O(m)** — Python's sorting algorithm uses additional space for sorting.

## Key Learning

Python's `sort()` with a **custom `key` function** makes it easy to sort a 2D list based on a specific column or element within each row.
