# LeetCode 1021 - Remove Outermost Parentheses

## Problem

Given a valid parentheses string `s`, remove the outermost parentheses of every primitive substring and return the resulting string.

## Approach

1. Initialize an empty `stack` to track open parentheses and a `result` list to store the remaining characters.
2. Traverse each character in the string.
3. If the character is `'('`:
   - Append it to `result` only if the stack is not empty.
   - Push it onto the stack.
4. If the character is `')'`:
   - Pop the matching opening parenthesis from the stack.
   - Append it to `result` only if the stack is still not empty.
5. Join the characters in `result` and return the final string.

```
stack = []result = []for char in s:    if char == '(':        if stack:            result.append(char)        stack.append(char)    else:        stack.pop()        if stack:            result.append(char)return "".join(result)
```

## Python Concepts Used

- Lists as stacks
- `append()` and `pop()`
- `for` loops
- Conditional statements
- Boolean evaluation of lists
- `join()` for string construction

## Time Complexity

O(n), where `n` is the length of the string, because each character is processed once.

## Space Complexity

O(n) for the stack and result list in the worst case.

## Key Learning

The stack tracks the nesting depth of parentheses. The outermost opening parenthesis is skipped when the stack is empty, and the outermost closing parenthesis is skipped when the stack becomes empty after popping.
