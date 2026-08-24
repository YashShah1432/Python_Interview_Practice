# LeetCode 1137 - N-th Tribonacci Number

## Problem

Given an integer `n`, return the `n`th Tribonacci number.

The Tribonacci sequence is defined as:

```text
T0 = 0
T1 = 1
T2 = 1
Tn = Tn-1 + Tn-2 + Tn-3
```

## Approach

Create a list to store the Tribonacci sequence:

```python
result = []
```

Handle the first three values:

```python
if i == 0 or i == 1:
    result.append(i)
elif i == 2:
    result.append(1)
```

For every subsequent value, add the previous three values:

```python
result.append(result[i-1] + result[i-2] + result[i-3])
```

Finally, return the `n`th value:

```python
return result[n]
```

## Python Concepts Used

* Lists
* `for` loop
* `range()`
* `if-elif-else`
* List indexing
* `append()`
* Arithmetic operations
* `return` statement

## Time Complexity

**O(n)**

The sequence is calculated from `0` to `n`.

## Space Complexity

**O(n)**

The `result` list stores all Tribonacci values up to `n`.

## Key Learning

The key idea is using **dynamic programming with a list** to store previously calculated Tribonacci values and use the previous three values to calculate the next one.
