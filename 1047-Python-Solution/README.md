# LeetCode 1047 - Remove All Adjacent Duplicates In String

## Problem

Given a string `s`, repeatedly remove pairs of adjacent equal characters until no adjacent duplicates remain. Return the resulting string.

## Approach

1. Use a list `st` as a stack.
2. Traverse each character in the string.
3. If the stack is empty or its last character is different from the current character, add the character.
4. If the last character is the same, remove it using `pop()`.
5. Join the remaining characters to form the final string.

```python
st = []

for ch in s:
    if not st or st[-1] != ch:
        st.append(ch)
    else:
        st.pop()

return "".join(st)
```

## Python Concepts Used

- Lists
- Stack implementation using a list
- `append()`
- `pop()`
- Negative indexing
- `for` loops
- `join()`
- Conditional statements

## Time Complexity

**O(n)**, where `n` is the length of the string.

## Space Complexity

**O(n)** in the worst case for the stack.

## Key Learning

A list can be used as a **stack** in Python. By comparing each character with the top of the stack, adjacent duplicates can be removed efficiently in a single traversal.
