# LeetCode 2859 - Sum of Values at Indices With K Set Bits

## Problem

Given an integer array `nums` and an integer `k`, calculate the sum of elements whose **indices have exactly `k` set bits** in their binary representation.

## Approach

1. Initialize `total` to `0`.
2. Iterate through all indices of `nums`.
3. Convert each index to binary using `bin()`.
4. Count the number of `1`s using `.count("1")`.
5. If the number of set bits equals `k`, add `nums[i]` to `total`.
6. Return the final sum.

```python
total = 0

for i in range(len(nums)):
    if bin(i).count("1") == k:
        total += nums[i]

return total
```

## Python Concepts Used

* **`bin()`** – Converts an integer into its binary representation.
* **`count()`** – Counts the number of `1` bits in the binary string.
* **For loop** – Iterates through all array indices.
* **List indexing** – Accesses the value at each index.
* **Modulo/bit representation concepts** – Identify indices based on their binary set bits.

## Time Complexity

**O(n × log n)** — For each of the `n` indices, converting to binary and counting set bits takes O(log n).

## Space Complexity

**O(log n)** — The binary representation of an index requires O(log n) space.

## Key Learning

The `bin()` function provides a simple way to work with the **binary representation of numbers**, and counting `"1"` characters can be used to determine the number of set bits.
