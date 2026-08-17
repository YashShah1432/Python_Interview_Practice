# LeetCode 1534 - Count Good Triplets

## Problem

Given an integer array `arr` and three integers `a`, `b`, and `c`, count the number of triplets `(i, j, k)` where:

```text
i < j < k
```

and all three conditions are satisfied:

```text
|arr[i] - arr[j]| <= a
|arr[j] - arr[k]| <= b
|arr[i] - arr[k]| <= c
```

## Approach

Use three nested loops to generate every possible triplet while maintaining the required order:

```python id="l2p9k1"
for i in range(0, len(arr)):
    for j in range(i + 1, len(arr)):
        for k in range(j + 1, len(arr)):
```

First check the condition between `arr[i]` and `arr[j]`:

```python id="v9d2nx"
if abs(arr[i] - arr[j]) <= a:
```

Then check the remaining two conditions:

```python id="x7k4pq"
if (abs(arr[j] - arr[k]) <= b) and (abs(arr[i] - arr[k]) <= c):
    count += 1
```

If all three conditions are satisfied, increment the triplet count.

## Python Concepts Used

* Nested `for` loops
* `range()`
* Array indexing
* `abs()`
* Conditional statements
* Comparison operators
* Counter variable
* `return` statement

## Time Complexity

**O(n³)**

Three nested loops are used to examine possible triplets.

## Space Complexity

**O(1)**

Only the `count` variable and loop variables are used.

## Key Learning

The key idea is to use **nested loops with increasing starting positions** to guarantee `i < j < k`. Each candidate triplet is then checked against the three given conditions.
