# LeetCode 1863 - Sum of All Subset XOR Totals

## Problem

Given an integer array `nums`, find the sum of the XOR totals of **all possible non-empty subsets**.

## Approach

Use `combinations()` to generate every possible subset of `nums`:

```python id="x7m4qp"
for i in range(1, len(nums) + 1):
    for combo in combinations(nums, i):
```

For each subset, use `reduce()` with the XOR operator to calculate its XOR total:

```python id="q4n8vz"
reduce(operator.xor, combo)
```

Store each XOR result in `subset` and return their sum:

```python id="h2k6ws"
return sum(subset)
```

genui{"learning_viz":{"type_id":"COMBINATION_FORMULA"}}

## Python Concepts Used

* Lists
* Nested `for` loops
* `combinations()`
* `reduce()`
* `operator.xor`
* Bitwise XOR operator
* `sum()`
* `return` statement

## Time Complexity

**O(2ⁿ × n)**

There are `2ⁿ - 1` non-empty subsets, and calculating the XOR of each subset can take up to O(n).

## Space Complexity

**O(2ⁿ)**

The `subset` list stores the XOR result of every non-empty subset.

## Key Learning

The key idea is to **generate every possible non-empty subset**, calculate the XOR of each subset, and then add all the XOR totals together.
