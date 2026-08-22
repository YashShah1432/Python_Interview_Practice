# LeetCode 3300 - Minimum Element After Replacement With Digit Sum

## Problem

Given an integer array `nums`, replace each element with the **sum of its digits** and return the minimum resulting value.

## Approach

For each number, extract its digits using `% 10` and add them to `total`:

```python
d = num % 10
num //= 10
total += d
```

Store the digit sum of each number in `result`:

```python
result.append(total)
```

Finally, return the minimum digit sum:

```python
return min(result)
```

## Python Concepts Used

* Lists
* `for` loop
* `while` loop
* Modulo operator `%`
* Integer division `//`
* `append()`
* `min()`
* Variables
* `return` statement

## Time Complexity

**O(n × d)**

Where `n` is the number of elements and `d` is the maximum number of digits in an element.

## Space Complexity

**O(n)**

The `result` list stores the digit sum of each element.

## Key Learning

The key idea is to **extract each digit using `% 10` and remove it using `// 10`**, calculate the digit sum for every number, and then find the minimum sum.
