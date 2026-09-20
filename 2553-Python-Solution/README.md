# LeetCode 2553 - Separate the Digits in an Array

## Problem

Given an array of positive integers `nums`, separate every number into its individual digits while preserving their original order.

## Approach

1. Use a nested list comprehension to iterate through every number in `nums`.
2. Convert each number to a string using `str()`.
3. Iterate through each character of the resulting string.
4. Convert each character back to an integer using `int()`.
5. Store all digits in a single list.

```python
return [int(char) for num in nums for char in str(num)]
```

## Python Concepts Used

* **List comprehension** – Create the result list concisely.
* **Nested iteration** – Iterate through numbers and their individual digits.
* **`str()`** – Convert each number into a string.
* **`int()`** – Convert each digit character back into an integer.
* **String iteration** – Process each digit individually.

## Time Complexity

**O(n × d)** — Where `n` is the number of elements and `d` is the average number of digits in each number.

## Space Complexity

**O(n × d)** — The result list contains every individual digit.

## Key Learning

A **nested list comprehension** can efficiently flatten the digits of multiple numbers into a single list while keeping their original order.
