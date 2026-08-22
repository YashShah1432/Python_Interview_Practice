# LeetCode 3516 - Find Closest Person

## Problem

Given three integers representing the positions of two people and a target position, determine which person is **closer to the target**.

Return:

* `1` if the first person is closer.
* `2` if the second person is closer.
* `0` if both are equally close.

## Approach

Calculate the distance of each person from the target using the absolute difference:

```python
abs(x - z)
```

Compare the two distances:

```python
if abs(x - z) < abs(y - z):
    return 1
elif abs(x - z) > abs(y - z):
    return 2
else:
    return 0
```

If both distances are equal, return `0`.

## Python Concepts Used

* Integers
* Variables
* `abs()`
* Comparison operators
* `if-elif-else`
* `return` statement

## Time Complexity

**O(1)**

Only a constant number of calculations are performed.

## Space Complexity

**O(1)**

Only a constant amount of extra space is used.

## Key Learning

The key idea is to **compare the absolute distances of both people from the target** to determine which person is closer.
