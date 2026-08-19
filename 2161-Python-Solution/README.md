# LeetCode 2161 - Partition Array According to Given Pivot

## Problem

Given an integer array `nums` and an integer `pivot`, rearrange the array so that:

* Elements **less than** `pivot` come first.
* Elements **equal to** `pivot` come next.
* Elements **greater than** `pivot` come last.

The relative order of elements within each group should remain unchanged.

## Approach

Create three lists to store the three groups:

```python id="x4c5ha"
smaller = []
equal = []
bigger = []
```

Iterate through each number and place it into the appropriate list:

```python id="v1b6zq"
if num < pivot:
    smaller.append(num)
elif num == pivot:
    equal.append(num)
else:
    bigger.append(num)
```

Finally, concatenate the three lists:

```python id="4f5f3j"
result = smaller + equal + bigger
```

Return the result.

## Python Concepts Used

* Lists
* `for` loop
* `if-elif-else`
* Comparison operators
* `append()`
* List concatenation `+`
* `return` statement

## Time Complexity

**O(n)**

The array is traversed once.

## Space Complexity

**O(n)**

Three lists are used to store the elements.

## Key Learning

The key idea is to **separate elements into three groups** based on their relationship with the pivot, then concatenate the groups while preserving their original order.
