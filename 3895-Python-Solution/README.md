# LeetCode 3895 - Count Substrings With K-Frequency Characters

## Problem

Given an array of integers `nums` and a digit `digit`, count how many times the given digit appears across all the numbers in `nums`.

## Approach

1. Initialize an empty string `string`.
2. Convert every number in `nums` to a string and concatenate them.
3. Traverse the resulting string character by character.
4. Compare each character with the string representation of `digit`.
5. Increment `count` whenever they match.
6. Return the total count.

```python
string = ""

for num in nums:
    string += str(num)

count = 0

for char in string:
    if char == str(digit):
        count += 1

return count
```

## Python Concepts Used

* **Lists** – Store the input numbers.
* **`str()`** – Convert numbers and the target digit into strings.
* **String concatenation** – Combine all numbers into one string.
* **For loop** – Traverse numbers and individual characters.
* **String comparison** – Compare each character with the target digit.
* **Counter variable** – Track the total occurrences.

## Time Complexity

**O(n × d)** — Where `n` is the number of elements and `d` is the average number of digits in each number.

## Space Complexity

**O(n × d)** — The combined string stores all digits from the input numbers.

## Key Learning

Converting numbers into strings provides a simple way to **process and count individual digits** across multiple integers.
