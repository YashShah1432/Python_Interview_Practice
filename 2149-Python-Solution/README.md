# LeetCode 2149 - Rearrange Array Elements by Sign

## Problem

Given an array containing an equal number of positive and negative integers, rearrange the elements so that positive and negative numbers alternate, starting with a positive number.

## Approach

1. Create separate lists for positive and negative numbers.
2. Traverse `nums` and place each element into the appropriate list.
3. Iterate through half the length of `nums`.
4. Append one positive number followed by one negative number to `result`.
5. Return the rearranged array.

```python
positive = []
negative = []
result = []

for ele in nums:
    positive.append(ele) if ele >= 0 else negative.append(ele)

for i in range(int(len(nums) / 2)):
    result.append(positive[i])
    result.append(negative[i])

return result
```

## Python Concepts Used

- Lists
- `for` loops
- Conditional expression
- List `append()`
- `len()`
- Integer conversion using `int()`
- List indexing

## Time Complexity

**O(n)** because the array is traversed to separate the elements and then traversed again to construct the result.

## Space Complexity

**O(n)** for the `positive`, `negative`, and `result` lists.

## Key Learning

Separating elements into positive and negative lists makes it simple to construct an alternating array. Keeping the two groups separately also preserves their relative order during rearrangement.
