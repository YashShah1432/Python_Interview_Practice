# LeetCode 1877 - Minimize Maximum Pair Sum in Array

## Problem

Given an array of even length, pair the elements so that the maximum pair sum is as small as possible. Return the minimized maximum pair sum.

## Approach

1. Calculate the number of pairs as `len(nums) / 2`.
2. Sort the array in ascending order.
3. Pair the smallest element with the largest element, the second smallest with the second largest, and so on.
4. Store each pair sum in `result`.
5. Return the maximum pair sum.

```python
n = int(len(nums) / 2)
nums.sort()
result = []

for i in range(n):
    result.append(nums[i] + nums[len(nums) - i - 1])

return max(result)
```

## Python Concepts Used

- Lists
- `len()`
- `int()` for integer conversion
- `sort()`
- Indexing
- `for` loop
- `append()`
- `max()`

## Time Complexity

**O(n log n)** due to sorting the array.

## Space Complexity

**O(n)** for storing the pair sums in the `result` list.

## Key Learning

After sorting, pairing the smallest element with the largest element helps balance the pair sums. The maximum among these pair sums gives the minimized maximum pair sum.
