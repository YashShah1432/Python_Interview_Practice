# LeetCode 3668 - Restore Finishing Order

## Problem

Given an array `order` representing the finishing order and an array `friends` containing the friends, return the friends in the same order in which they appear in `order`.

## Approach

Convert both arrays into sets and find the elements in `order` that are not present in `friends`:

```python
not_in_list = list(set(order) - set(friends))
```

Remove those elements from `order`:

```python
for num in not_in_list:
    order.remove(num)
```

The remaining elements in `order` are the friends in their original finishing order.

## Python Concepts Used

* Lists
* Sets
* `set()`
* Set difference `-`
* `list()`
* `for` loop
* `remove()`
* `return` statement

## Time Complexity

**O(n)**

The sets are created in O(n) average time, and the elements not in `friends` are removed from `order`.

## Space Complexity

**O(n)**

Sets and the `not_in_list` require additional space.

## Key Learning

The key idea is using **set difference to identify elements that are not friends**, then removing them from `order` while preserving the relative order of the remaining elements.
