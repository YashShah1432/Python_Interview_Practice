# LeetCode 1281 - Subtract the Product and Sum of Digits of an Integer

## Problem

Given an integer `n`, calculate the **product of its digits** and the **sum of its digits**, then return the difference between them.

```text
Product of digits - Sum of digits
```

## Approach

Extract each digit using the modulo operator:

```python
n % 10
```

Then remove the last digit using integer division:

```python
n = n // 10
```

Store all digits in an array:

```python
arr.append(n % 10)
```

After extracting all digits, calculate the product using `math.prod()` and the sum using `sum()`:

```python
math.prod(arr) - sum(arr)
```

## Python Concepts Used

* `while` loop
* Lists
* Modulo operator `%`
* Integer division `//`
* `append()`
* `math.prod()`
* `sum()`
* Function parameters
* `return` statement

## Time Complexity

**O(d)**

Where `d` is the number of digits in `n`.

## Space Complexity

**O(d)**

The `arr` list stores all the digits of `n`.

## Key Learning

The key idea is to repeatedly use **`% 10` to extract the last digit** and **`// 10` to remove the last digit**. This is a common technique for processing the individual digits of an integer.
