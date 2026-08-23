# LeetCode 3731 - Find Missing Elements

## Problem

Given an integer array `nums`, find all the elements missing between the **smallest and largest values** in the array.

## Approach

First, sort the array:

```python
nums.sort()
```

Create a list containing all numbers from the smallest to the largest value:

```python
for i in range(nums[0], nums[len(nums)-1]+1):
    new_nums.append(i)
```

Use set difference to find the numbers that are present in `new_nums` but missing from `nums`:

```python
result = list(set(new_nums) - set(nums))
```

Sort the result and return it:

```python
result.sort()
return result
```

## Python Concepts Used

* Lists
* `sort()`
* `for` loop
* `range()`
* Sets
* Set difference `-`
* `list()`
* List indexing
* `append()`
* `return` statement

## Time Complexity

**O(n log n)**

Sorting the input array takes O(n log n), while the remaining operations are linear on average.

## Space Complexity

**O(n)**

Additional lists and sets are used to store the numbers.

## Key Learning

The key idea is to **generate the complete range between the minimum and maximum values** and use **set difference** to identify the missing elements.
