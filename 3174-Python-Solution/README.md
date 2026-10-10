# LeetCode 3174 - Clear Digits

## Problem

Given a string `s` containing lowercase English letters and digits, repeatedly remove the first digit and the closest non-digit character to its left. Return the resulting string.

## Approach

1. Initialize an empty list `stack`.
2. Traverse each character in the string.
3. If the stack is not empty and the current character is a digit, remove the last character from the stack using `pop()`.
4. Otherwise, append the current character to the stack.
5. Join the remaining characters and return the resulting string.

```
stack = []for char in s:    if stack and char.isdigit():        stack.pop()    else:        stack.append(char)return "".join(stack)
```

## Python Concepts Used

- Lists as stacks
- `append()` and `pop()`
- `for` loops
- Conditional statements
- `isdigit()` for checking digits
- `join()` for string construction
- Boolean evaluation of lists

## Time Complexity

O(n), where `n` is the length of the string, because each character is processed once.

## Space Complexity

O(n) for storing characters in the stack in the worst case.

## Key Learning

A stack efficiently removes the closest character to the left of each digit. The `isdigit()` method identifies digits, while `pop()` removes the most recently stored character.
