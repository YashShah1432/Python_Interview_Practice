# LeetCode 2798 - Number of Employees Who Met the Target

## Problem

Given an integer array `hours` and an integer `target`, count the number of employees who worked at least `target` hours.

## Approach

Iterate through each employee's working hours:

```python
for i in range(len(hours)):
```

Check whether the employee worked at least the target number of hours:

```python
if hours[i] >= target:
    count += 1
```

Finally, return the total count:

```python
return count
```

## Python Concepts Used

* Lists
* `for` loop
* `range()`
* List indexing
* Comparison operators
* Counter variable
* `return` statement

## Time Complexity

**O(n)**

The `hours` array is traversed once.

## Space Complexity

**O(1)**

Only the `count` variable is used.

## Key Learning

The key idea is to **iterate through the array and count every employee whose working hours are greater than or equal to the target**.
