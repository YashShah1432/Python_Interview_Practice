# LeetCode 20 - Valid Parentheses

## Problem

Given a string `s` containing the characters `(`, `)`, `{`, `}`, `[` and `]`, determine whether the input string contains **valid parentheses**.

A valid string must have:

* Every opening bracket closed by the same type of bracket.
* Brackets closed in the correct order.
* Every closing bracket have a corresponding opening bracket.

## Approach

Use a **stack** to keep track of opening brackets.

When an opening bracket is encountered, add it to the stack:

```python
stack.append(char)
```

When a closing bracket is encountered, check whether the top of the stack contains its corresponding opening bracket.

If they match, remove the opening bracket:

```python
stack.pop()
```

If they do not match, return `False`.

After processing all characters, the stack must be empty for the parentheses to be valid.

## Python Concepts Used

* Lists
* Stack data structure
* `for` loop
* `append()`
* `pop()`
* `len()`
* Conditional statements
* `return` statement

## Time Complexity

**O(n)**

Each character is processed once.

## Space Complexity

**O(n)**

In the worst case, all characters can be opening brackets and stored in the stack.

## Key Learning

The key idea is using a **stack (LIFO)** because the most recently opened bracket must be the first one to be closed. This makes stacks ideal for checking balanced and properly nested parentheses.
