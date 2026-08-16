# LeetCode 1313 - Decompress Run-Length Encoded List

## Problem

Given an integer array `nums` where every pair of elements represents:

```text
[frequency, value]
```

Decompress the list by repeating `value` exactly `frequency` times.

## Approach

Iterate through `nums` by taking every second element as the frequency:

```python
for i in range(0, len(nums), 2):
```

For each pair:

* `nums[i]` represents the frequency.
* `nums[i + 1]` represents the value.

Use a `while` loop to append the value according to its frequency:

```python
while nums[i] > 0:
    result.append(nums[i + 1])
    nums[i] -= 1
```

Finally, return the decompressed list.

## Python Concepts Used

* Lists
* `for` loop
* `while` loop
* `range()` with step
* `append()`
* Array indexing
* Arithmetic operations
* `return` statement

## Time Complexity

**O(n + k)**

Where `n` is the length of the input array and `k` is the number of elements in the decompressed result.

## Space Complexity

**O(k)**

The `result` list stores all elements of the decompressed array.

## Key Learning

The key idea is to process the input in **pairs of frequency and value** and use the frequency to determine how many times each value should be added to the result.
