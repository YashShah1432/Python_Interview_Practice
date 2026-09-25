# LeetCode 14 - Longest Common Prefix

## Problem

Given an array of strings `strs`, find the **longest common prefix** shared by all strings. If there is no common prefix, return an empty string.

## Approach

1. Check if the input list is empty. If so, return `""`.
2. Iterate through each character of the first string.
3. Compare that character with the character at the same position in every other string.
4. If a string is too short or the characters don't match, return the prefix up to the current index.
5. If all characters match, return the first string.

```python
if not strs:
    return ""

for i in range(len(strs[0])):
    char = strs[0][i]

    for s in strs[1:]:
        if i == len(s) or s[i] != char:
            return strs[0][:i]

return strs[0]
```

## Python Concepts Used

* **List indexing** – Access characters at specific positions.
* **String slicing** – Extract the common prefix using `strs[0][:i]`.
* **Nested loops** – Compare characters across all strings.
* **List slicing** – Iterate through all strings except the first using `strs[1:]`.
* **Conditional statements** – Detect mismatched or missing characters.

## Time Complexity

**O(n × m)** — Where `n` is the number of strings and `m` is the length of the shortest relevant prefix.

## Space Complexity

**O(m)** — String slicing creates the resulting prefix.

## Key Learning

When finding a common property across multiple strings, comparing characters at the **same index** allows the common prefix to be identified as soon as a mismatch occurs.
