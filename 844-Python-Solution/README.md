# LeetCode 844 - Backspace String Compare

## Problem

Given two strings `s` and `t`, determine whether they are equal after processing all backspace characters (`#`). A backspace removes the previous character if one exists.

## Approach

1. Create two stacks, `stack_s` and `stack_t`, to process the strings independently.
2. Traverse each string character by character.
3. If the character is `#`, remove the top element from the stack if it is not empty.
4. Otherwise, append the character to the stack.
5. Compare both stacks and return `True` if they are equal; otherwise, return `False`.

```
stack_s = []stack_t = []for char in s:    if char == "#":        if stack_s:            stack_s.pop()    else:        stack_s.append(char)for char in t:    if char == "#":        if stack_t:            stack_t.pop()    else:        stack_t.append(char)return stack_s == stack_t
```

## Python Concepts Used

- Lists as stacks
- `append()` and `pop()`
- `for` loops
- Conditional statements
- Boolean evaluation
- List comparison

## Time Complexity

O(n + m), where `n` and `m` are the lengths of strings `s` and `t`, respectively.

## Space Complexity

O(n + m) for storing the processed characters in both stacks.

## Key Learning

A stack provides a simple way to simulate backspace operations. Each `#` removes the most recently added character, and comparing the final stacks determines whether the processed strings are equal.
