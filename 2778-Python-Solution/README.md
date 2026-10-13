# LeetCode 2778 - Sum of Squares of Special Elements

## Problem

Given a 0-indexed integer array `nums`, calculate the sum of squares of all special elements. An element `nums[i]` is special if the length of the array is divisible by its 1-based index.

## Approach

1. Initialize `result = 0` and calculate the array length `n`.
2. Iterate through the 1-based indices from `1` to `n`.
3. Check whether `n % i == 0` to determine if the index divides the array length evenly.
4. If the index is special, add the square of `nums[i - 1]` to `result`.
5. Return the final sum.

```
result = 0n = len(nums)for i in range(1, n + 1):    if n % i == 0:        result = result + (nums[i - 1] * nums[i - 1])return result
```

## Python Concepts Used

- Lists and indexing
- `len()`
- `for` loops and `range()`
- Modulo operator (`%`)
- Conditional statements
- Arithmetic operations
- Accumulator variable

## Time Complexity

O(n) because the solution checks every index in the array once.

## Space Complexity

O(1) because only a constant amount of extra space is used.

## Key Learning

The modulo operator (`%`) helps identify special indices by checking whether the array length is divisible by an index. Since Python lists use zero-based indexing, `nums[i - 1]` accesses the element corresponding to the 1-based index `i`.
