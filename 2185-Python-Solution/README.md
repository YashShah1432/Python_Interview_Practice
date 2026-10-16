# LeetCode 2185 - Counting Words With a Given Prefix

## Problem

Given a list of strings `words` and a string `pref`, count how many words in the list start with the given prefix.

## Approach

1. Initialize `count = 0` to track matching words.
2. Iterate through each word in `words`.
3. Use `startswith(pref)` to check whether the word begins with the given prefix.
4. If the word matches, increment `count` by one.
5. Return the final count.

```
count = 0for word in words:    if word.startswith(pref):        count += 1return count
```

## Python Concepts Used

- Lists and string iteration
- `for` loops
- `startswith()` string method
- Conditional statements
- Counter variable
- `return`

## Time Complexity

O(n × m), where `n` is the number of words and `m` is the maximum length of a word, since checking a prefix can take up to O(m) time.

## Space Complexity

O(1) because only a constant amount of extra space is used.

## Key Learning

The `startswith()` method provides a simple way to check whether a string begins with a specific prefix, avoiding the need to manually compare individual characters.
