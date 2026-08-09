# LeetCode 1480 - Running Sum of 1d Array

## Problem
Given an array of integers `nums`, calculate the **running sum** of the array.

The running sum at index `i` is the sum of all elements from index `0` to index `i`.

## Approach
1. Create an empty list `result` to store the running sums.
2. Initialize `total` to `0`.
3. Iterate through every number in `nums`.
4. Add the current number to `total`.
5. Append the updated `total` to the `result` list.
6. Return the resulting list.

### Example

For:

```text
nums = [1, 2, 3, 4]
```

The running sum is:

```text
[1, 3, 6, 10]
```

Because:

```text
1
1 + 2 = 3
1 + 2 + 3 = 6
1 + 2 + 3 + 4 = 10
```

## Python Concepts Used
- Lists
- `for` Loop
- Accumulator Variable
- `append()`
- Array Traversal

## Time Complexity
**O(n)**

The array is traversed once.

## Space Complexity
**O(n)**

The `result` list stores `n` running-sum values.
