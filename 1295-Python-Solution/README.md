# LeetCode 1295 - Find Numbers with Even Number of Digits

## Problem

Given an integer array `nums`, return the number of integers that contain an **even number of digits**.

## Approach

Iterate through each number in the array and count its digits using `% 10` and `// 10`.

First, check whether the number has at least two digits:

```python
if num >= 10:
```

Then repeatedly extract digits:

```python
while num > 0:
    digit += 1
    num = num // 10
```

After counting the digits, check whether the digit count is even:

```python
if digit % 2 == 0:
    count += 1
```

Finally, return the total count.

## Python Concepts Used

* `for` loop
* `while` loop
* Lists
* Modulo operator `%`
* Integer division `//`
* Conditional statements
* Counter variables
* `return` statement

## Time Complexity

**O(n × d)**

Where `n` is the number of elements and `d` is the maximum number of digits in an element.

## Space Complexity

**O(1)**

Only a few variables are used regardless of the input size.

## Key Learning

The key idea is to count the digits of each number using **`% 10` and `// 10`**, then use the modulo operator to determine whether the digit count is even.
