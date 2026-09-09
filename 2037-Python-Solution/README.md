# LeetCode 2037 - Minimum Number of Moves to Seat Everyone

## Problem

Given two arrays `seats` and `students`, where each element represents a position, find the **minimum number of moves** needed to move every student to a seat.

A student can move one position at a time.

## Approach

First, sort both arrays so that the closest positions can be matched:

```python
seats.sort()
students.sort()
```

Then compare the corresponding positions of each seat and student.

If the student's position is greater than the seat:

```python
count += students[i] - seats[i]
```

If the student's position is smaller:

```python
count += seats[i] - students[i]
```

This calculates the absolute distance between each student and their assigned seat.

Finally, return the total number of moves.

## Python Concepts Used

* Lists
* `sort()`
* `for` loop
* `range()`
* List indexing
* Conditional statements
* Arithmetic operations
* Counter variable
* `continue`
* `return` statement

## Time Complexity

**O(n log n)**

Sorting both arrays takes O(n log n), and comparing the elements takes O(n).

## Space Complexity

**O(1)**

The sorting is performed directly on the input arrays, and only a few variables are used.

## Key Learning

The key idea is to **sort both arrays and match students with seats in the same order**, then add the distance between each corresponding pair.
