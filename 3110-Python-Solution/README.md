# LeetCode 3110 - Score of a String

## Problem

Given a string `s`, calculate the **score of the string** by finding the absolute difference between the ASCII values of every pair of adjacent characters and adding them together.

## Approach

Iterate through the string up to the second-last character:

```python id="z2e8lq"
for i in range(0, len(s)-1):
```

Use `ord()` to get the ASCII value of each character and calculate their absolute difference:

```python id="7c4m2n"
abs(ord(s[i]) - ord(s[i+1]))
```

Add each difference to `result`:

```python id="g8q5wt"
result += abs(ord(s[i]) - ord(s[i+1]))
```

Finally, return the total score.

## Python Concepts Used

* Strings
* `for` loop
* `range()`
* String indexing
* `ord()`
* `abs()`
* Arithmetic operations
* `return` statement

## Time Complexity

**O(n)**

The string is traversed once.

## Space Complexity

**O(1)**

Only the `result` variable is used.

## Key Learning

The key idea is using **`ord()` to convert characters into their ASCII values** and calculating the absolute difference between consecutive characters.
