# LeetCode 3467 - Transform Array by Parity

## Problem

Given an integer array `nums`, transform each element into:

* `0` if the element is even.
* `1` if the element is odd.

Then sort the resulting array in ascending order.

## Approach

Iterate through every element and replace it with `0` or `1` based on its parity:

```python
nums[i] = 0 if nums[i] % 2 == 0 else 1
```

Then sort the modified array:

```python
nums.sort()
```

Finally, return the transformed array.

## Python Concepts Used

* Lists
* `for` loop
* `range()`
* List indexing
* Modulo operator `%`
* Conditional expression
* `sort()`
* `return` statement

## Time Complexity

**O(n log n)**

The transformation takes O(n), while sorting takes O(n log n).

## Space Complexity

**O(1)**

The transformation is performed directly on the input array.
