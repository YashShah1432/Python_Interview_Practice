# LeetCode 1832 - Check if the Sentence Is Pangram

## Problem

Given a string `sentence`, determine whether it is a pangram. A pangram contains every lowercase English letter from `a` to `z` at least once.

## Approach

1. First, check if the sentence length is at least `26`. If not, it cannot contain all 26 letters.
2. Convert every character into its ASCII value using `ord()`.
3. Store the ASCII values in a list.
4. Convert the list into a `set` to remove duplicate characters.
5. Sort the unique ASCII values.
6. If there are exactly `26` unique values, return `True`; otherwise, return `False`.

```python
if len(sentence) >= 26:
    result = []

    for char in sentence:
        result.append(ord(char))

    ans = set(result)
    final_ans = sorted(list(ans))

    return True if len(final_ans) == 26 else False
else:
    return False
```

## Python Concepts Used

* `len()` for checking string length
* `for` loop for character traversal
* `ord()` for converting characters to ASCII values
* Lists and `append()`
* `set()` for removing duplicates
* `sorted()` for sorting unique values
* Conditional expressions
* Boolean return values

## Time Complexity

**O(n + k log k)**, where `n` is the length of the sentence and `k` is the number of unique characters. Since there can be at most 26 lowercase English letters, `k ≤ 26`, making this effectively **O(n)**.

## Space Complexity

**O(n)** for the `result` list in the worst case, along with the set of unique characters.

## Key Learning

A `set` is useful for finding the number of unique characters because it automatically removes duplicates. Using `ord()` also provides a way to represent characters numerically and compare their uniqueness.
