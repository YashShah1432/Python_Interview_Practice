# LeetCode 2520 - Count the Digits That Divide a Number

## Problem

Given an integer `num`, count how many digits in `num` divide `num` evenly. Every digit is guaranteed to be non-zero.

## Approach

1. Convert `num` into a string to iterate through its individual digits.
2. Convert each digit back to an integer.
3. Check whether `num` is divisible by the digit using the modulo operator `%`.
4. If the remainder is `0`, increment the count.
5. Return the total count.

```python
count = 0

for digit in str(num):
    if num % int(digit) == 0:
        count += 1

return count
```

## Python Concepts Used

* **`str()`** – Convert the number into a string for digit-wise iteration.
* **For loop** – Iterate through each digit.
* **`int()`** – Convert each character back into an integer.
* **Modulo `%`** – Check whether the digit divides the number evenly.
* **Counter variable** – Track the number of digits that divide `num`.

## Time Complexity

**O(d)** — Where `d` is the number of digits in `num`.

## Space Complexity

**O(d)** — Converting the number to a string requires space proportional to the number of digits.

## Key Learning

Converting an integer to a **string** is a simple way to process its individual digits, while the **modulo operator** can be used to check divisibility.
