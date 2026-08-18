# LeetCode 3945 - Digit Frequency Score

## Problem

Given an integer `n`, calculate the **digit frequency score** by multiplying each unique digit by the number of times it appears, then adding all these values together.

## Approach

Convert `n` into a string and use `Counter` to count the frequency of each digit:

```python
freq = Counter(str(n))
```

Then iterate through each digit and its frequency:

```python
for digit, frequency in freq.items():
    result += int(digit) * frequency
```

Each digit is multiplied by its frequency and added to `result`.

## Python Concepts Used

* `Counter`
* Strings
* Dictionaries
* `for` loop
* `items()`
* `int()`
* Multiplication
* `return` statement

## Time Complexity

**O(d)**

Where `d` is the number of digits in `n`.

## Space Complexity

**O(d)**

The `Counter` stores the frequency of the digits.

## Key Learning

The key idea is using **`Counter` to efficiently calculate the frequency of each digit**, then using those frequencies to calculate the required score.
