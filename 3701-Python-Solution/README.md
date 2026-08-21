# LeetCode 3701 - Alternating Sum of Numbers

## Problem

Given an integer array `nums`, calculate the **alternating sum** of its elements.

The first element is added, the second is subtracted, the third is added, and so on.

```text
nums[0] - nums[1] + nums[2] - nums[3] + ...
```

## Approach

Create a reference to the input array:

```python
temp = nums
```

Iterate through the elements at odd indexes:

```python
for i in range(1, len(nums), 2):
```

For each element at an odd index, change its sign:

```python
temp[i] -= temp[i] * 2
```

This converts a positive value to negative and a negative value to positive.

Finally, calculate the sum:

```python
return sum(temp)
```

## Python Concepts Used

* Lists
* `for` loop
* `range()` with step
* List indexing
* Arithmetic operations
* `sum()`
* Variables
* `return` statement

## Time Complexity

**O(n)**

The array is traversed once.

## Space Complexity

**O(1)**

No additional array is created; `temp` references the original list.

## Key Learning

The key idea is to **change the sign of elements at odd indexes** so that a normal `sum()` produces the required alternating sum.
