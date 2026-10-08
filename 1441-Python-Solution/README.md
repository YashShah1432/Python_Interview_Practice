# LeetCode 1441 - Build an Array With Stack Operations

## Problem

Given a target array and an integer `n`, build the target array using only `"Push"` and `"Pop"` operations while reading numbers sequentially from `1` to `n`.

## Approach

1. Create an empty list `s` to store the operations.
2. Find the maximum number needed using `min(max(target), n)`.
3. Iterate from `1` to that maximum value.
4. Add `"Push"` for every number because each number is read from the stream.
5. If the current number is not present in `target`, add `"Pop"` to remove it.
6. Return the list of operations.

```python
s = []
length = min(max(target), n)

for i in range(length + 1):
    if i == 0:
        continue

    s.append("Push")

    if i not in target:
        s.append("Pop")

return s
```

## Python Concepts Used

- Lists
- `max()`
- `min()`
- `for` loops
- `in` membership operator
- `append()`
- Conditional statements

## Time Complexity

**O(n × m)**, where `n` is the range of numbers processed and `m` is the length of `target`, because `i not in target` performs a linear search through the target list.

## Space Complexity

**O(n)** for storing the operations in the result list.

## Key Learning

The `"Push"` operation is performed for every number encountered, while `"Pop"` is used to discard numbers that are not part of the target. This directly simulates the sequential stream of numbers and stack operations.
