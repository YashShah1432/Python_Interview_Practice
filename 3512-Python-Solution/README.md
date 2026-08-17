# LeetCode 3512 - Minimum Operations to Make Array Sum Divisible by K

## Problem

Given an integer array `nums` and an integer `k`, find the minimum number of operations needed to make the sum of all elements in `nums` divisible by `k`.

In one operation, an element can be decreased by `1`.

## Approach

Calculate the total sum of the array:

```python
sum(nums)
```

The remainder when dividing the sum by `k` tells us how many decrement operations are required:

```python
sum(nums) % k
```

If the sum is already divisible by `k`, the remainder is `0`, so no operations are required.

## Python Concepts Used

* Lists
* `sum()`
* Modulo operator `%`
* `return` statement
* Function parameters

## Time Complexity

**O(n)**

The `sum()` function traverses all elements of the array.

## Space Complexity

**O(1)**

No additional data structures are used.

## Key Learning

The key idea is that the **remainder of the total sum when divided by `k` directly gives the minimum number of decrement operations** needed to make the sum divisible by `k`.
