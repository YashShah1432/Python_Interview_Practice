# LeetCode 771 - Jewels and Stones

## Problem

Given two strings `jewels` and `stones`, determine how many stones are also jewels.

Each character in `jewels` represents a type of stone that is considered a jewel. Count how many characters in `stones` match any character in `jewels`.

## Approach

Use nested loops to compare every jewel with every stone.

For each character in `jewels`, iterate through all characters in `stones`. Whenever a stone matches the current jewel, increment the `count`.

```text
stone == jewel → count + 1
```

Finally, return the total count.

## Python Concepts Used

* Nested `for` loops
* Strings
* Character iteration
* Comparison operators
* Counter variable
* `return` statement

## Time Complexity

**O(n × m)**

Where `n` is the length of `jewels` and `m` is the length of `stones`.

## Space Complexity

**O(1)**

Only the `count` variable is used apart from the input strings.

## Key Learning

The key idea is to compare each stone against every jewel and count every match. This is a straightforward **nested-loop search** approach.
