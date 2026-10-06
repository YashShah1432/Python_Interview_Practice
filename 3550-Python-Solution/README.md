# LeetCode 3550 - Smallest Index With Digit Sum Equal to Index

## Problem

Given an array of integers, find the smallest index `i` such that the sum of the digits of `nums[i]` is equal to `i`. Return `-1` if no such index exists.

## Approach

1. Traverse the array from left to right.
2. If the current number is a single digit and equals its index, return the index directly.
3. Otherwise, convert the number to a string and calculate the sum of its digits.
4. If the digit sum equals the current index, return the index.
5. If no matching index is found, return `-1`.

```python
for i in range(0, len(nums)):
    if nums[i] <= 9 and nums[i] == i:
        return i
    else:
        total = 0
        for digit in str(nums[i]):
            total += int(digit)

        if total == i:
            return i

return -1
```

## Python Concepts Used

- Lists
- `for` loops
- String conversion using `str()`
- Integer conversion using `int()`
- String iteration
- Conditional statements
- Early `return`
- Digit sum calculation

## Time Complexity

**O(n × d)**, where `n` is the number of elements and `d` is the maximum number of digits in an element.

## Space Complexity

**O(d)** due to the temporary string representation of each number.

## Key Learning

Iterating through the array from left to right naturally finds the **smallest valid index**. Converting a number to a string provides a simple way to access and sum its individual digits.
