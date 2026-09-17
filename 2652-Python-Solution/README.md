# LeetCode 2652 - Sum Multiples

## Problem

Given an integer `n`, find the sum of all positive integers from `1` to `n` that are divisible by **3, 5, or 7**.

## Approach

1. Initialize `total` to `0`.
2. Iterate through all numbers from `1` to `n`.
3. Check if the current number is divisible by `3`, `5`, or `7`.
4. If it is divisible by at least one of them, add it to `total`.
5. Return the final sum.

```python
total = 0

for i in range(1, n + 1):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        total += i

return total
```

## Python Concepts Used

* **For loop** – Iterate through numbers from `1` to `n`.
* **`range()`** – Generate the required sequence of numbers.
* **Modulo `%`** – Check whether a number is divisible by `3`, `5`, or `7`.
* **Logical `or`** – Check multiple divisibility conditions.
* **Accumulator variable** – Store the running sum.

## Time Complexity

**O(n)** — Each number from `1` to `n` is checked once.

## Space Complexity

**O(1)** — Only the `total` variable is used.

## Key Learning

The **modulo operator `%`** is useful for checking divisibility, and multiple conditions can be combined using the logical `or` operator.
