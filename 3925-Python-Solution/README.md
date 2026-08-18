# LeetCode 3925 - Concatenate with Reverse

## Problem

Given an integer array `nums`, return a new array formed by concatenating the original array with its reverse.

For example:

```text
nums = [1, 2, 3]
```

The result is:

```text
[1, 2, 3, 3, 2, 1]
```

## Approach

Use Python list slicing to reverse the array:

```python
nums[::-1]
```

Then concatenate the original array with the reversed array:

```python
ans = nums + nums[::-1]
```

Finally, return the result.

## Python Concepts Used

* Lists
* List slicing `[::-1]`
* List concatenation `+`
* Variables
* `return` statement

## Time Complexity

**O(n)**

The original and reversed arrays are combined to create a result containing `2n` elements.

## Space Complexity

**O(n)**

The reversed array and resulting array require additional space.

## Key Learning

The key idea is using **`[::-1]` to reverse a list** and the `+` operator to concatenate two lists.
