# LeetCode 3751 - Total Waviness of Numbers

## Problem

Given two integers `num1` and `num2`, calculate the total **waviness** of all numbers in the range from `num1` to `num2`.

A digit is considered a peak or valley when it is either greater than both neighboring digits or smaller than both neighboring digits.

## Approach

Iterate through every number in the given range:

```python
for number in range(num1, num2+1):
```

Skip numbers with fewer than three digits:

```python
if number < 100:
    continue
```

Convert the number to a string so its individual digits can be accessed:

```python
num = str(number)
```

Check each digit except the first and last digit:

```python
for j in range(1, len(num)-1):
```

A digit contributes to waviness if it is greater than both neighbors or smaller than both neighbors:

```python
if (int(num[j]) > int(num[j-1]) and int(num[j]) > int(num[j+1])) or (int(num[j]) < int(num[j-1]) and int(num[j]) < int(num[j+1])):
    waviness += 1
```

Finally, return the total waviness.

## Python Concepts Used

* Integers
* Strings
* `for` loop
* `range()`
* String indexing
* `str()`
* `int()`
* Conditional statements
* Comparison operators
* `continue`
* Counter variable
* `return` statement

## Time Complexity

**O(n × d)**

Where `n` is the number of integers in the given range and `d` is the number of digits in each number.

## Space Complexity

**O(d)**

The number is converted into a string, requiring space proportional to its number of digits.

## Key Learning

The key idea is to **check each middle digit against its two neighboring digits**. If it is either greater than both or smaller than both, it contributes one to the total waviness.
