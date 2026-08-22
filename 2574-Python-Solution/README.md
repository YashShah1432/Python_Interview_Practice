# LeetCode 2574 - Left and Right Sum Differences

## Problem

Given an integer array `nums`, calculate the absolute difference between the sum of elements to the **left** and the sum of elements to the **right** of each index.

Return an array containing these differences.

## Approach

First, create a reversed copy of the array:

```python
reverse_num = nums[::-1]
```

Use two lists to store the cumulative left and right sums:

```python
left_sum = []
right_sum = []
```

For the first element, there are no elements on either side, so both sums are `0`.

For the remaining elements, calculate the cumulative sums:

```python
left_sum.append(left_sum[i - 1] + nums[i-1])
right_sum.append(right_sum[i - 1] + reverse_num[i-1])
```

Finally, calculate the absolute difference between the corresponding left and right sums:

```python
answer.append(abs(left_sum[i] - right_sum[len(nums)-i-1]))
```

## Python Concepts Used

* Lists
* List slicing `[::-1]`
* `for` loop
* `range()`
* List indexing
* `append()`
* `abs()`
* Cumulative sums
* `return` statement

## Time Complexity

**O(n)**

The array is traversed a constant number of times.

## Space Complexity

**O(n)**

Additional lists are used to store the reversed array, left sums, right sums, and result.

## Key Learning

The key idea is to calculate **cumulative sums from both directions** and then find the absolute difference between the left and right sums for each position.
