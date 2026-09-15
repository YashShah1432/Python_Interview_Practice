# LeetCode 1967 - Number of Strings That Appear as Substrings in Word

## Problem

Given a list of strings `patterns` and a string `word`, count how many strings in `patterns` appear as a **substring** of `word`.

## Approach

1. Initialize `count` to `0`.
2. Iterate through each `pattern` in `patterns`.
3. Use the `in` operator to check whether the pattern exists inside `word`.
4. If it exists, increment `count`.
5. Return the final count.

```python
count = 0

for pattern in patterns:
    if pattern in word:
        count += 1

return count
```

## Python Concepts Used

* **For loop** – Iterate through all patterns.
* **`in` operator** – Check whether a string exists as a substring.
* **Lists** – Store multiple pattern strings.
* **String operations** – Perform substring searching.
* **Counter variable** – Keep track of matching patterns.

## Time Complexity

**O(n × m)** — Where `n` is the number of patterns and `m` is the length of `word`.

## Space Complexity

**O(1)** — Only a counter variable is used apart from the input.

## Key Learning

Python's **`in` operator** provides a simple and readable way to check whether one string exists as a substring of another.
