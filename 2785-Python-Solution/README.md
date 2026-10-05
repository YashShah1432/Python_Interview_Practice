# LeetCode 2785 - Sort Vowels in a String

## Problem

Given a string `s`, sort only the vowels in the string in ascending order while keeping all consonants in their original positions.

## Approach

1. Create a list containing all uppercase and lowercase vowels.
2. Traverse the string and collect the ASCII-based values of all vowels.
3. Sort the collected vowel values.
4. Traverse the string again.
5. Replace each vowel position with the next sorted vowel while keeping consonants unchanged.
6. Join the characters to form the final string.

```python
vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
result = []
t = []
v_idx = 0

for i in range(len(s)):
    if s[i] in vowel:
        result.append(ord(s[i]) - ord('A'))

result.sort()

for i in range(len(s)):
    if s[i] in vowel:
        t.append(chr(result[v_idx] + ord('A')))
        v_idx += 1
    else:
        t.append(s[i])

return "".join(t)
```

## Python Concepts Used

- Lists
- Nested iteration over strings
- `ord()` for converting characters to numeric values
- `chr()` for converting numeric values back to characters
- `sort()`
- String indexing
- `join()` for constructing the final string
- Membership operator `in`

## Time Complexity

**O(n log n)**, where `n` is the length of the string. The sorting step takes up to `O(n log n)`.

## Space Complexity

**O(n)** for storing the vowels and the resulting character lists.

## Key Learning

Only the vowels need to be extracted and sorted. By traversing the original string again, the sorted vowels can be placed back while preserving the positions of all consonants.
