# LeetCode 2375 - Construct Smallest Number From DI String

## Problem

Given a pattern containing `'I'` (increasing) and `'D'` (decreasing), construct the **smallest number** using digits `1` to `n + 1` that follows the given pattern.

## Approach

1. Initialize an empty `result` list and a stack `num_stack`.
2. Iterate from `1` to `len(pattern) + 1`.
3. Add each number to the stack.
4. Whenever the current pattern character is `'I'`, or the end of the pattern is reached, pop all elements from the stack and add them to `result`.
5. Reversing consecutive numbers through the stack naturally handles `'D'` sequences.
6. Join the result digits into the final string.

```python
result = []
num_stack = []

for i in range(len(pattern) + 1):
    num_stack.append(i + 1)

    if i == len(pattern) or pattern[i] == 'I':
        while num_stack:
            result.append(str(num_stack.pop()))

return "".join(result)
```

## Python Concepts Used

* **Lists** – Store the result and stack elements.
* **Stack** – Use `append()` and `pop()` to process numbers in reverse order.
* **For loop** – Iterate through the required digits.
* **Conditional statements** – Detect `'I'` and the end of the pattern.
* **`join()`** – Combine the result digits into a single string.

## Time Complexity

**O(n)** — Each number is pushed onto and popped from the stack exactly once.

## Space Complexity

**O(n)** — The result list and stack can store up to `n + 1` elements.

## Key Learning

A **stack** is useful for handling consecutive decreasing (`D`) patterns because popping elements reverses their order automatically, allowing the smallest valid number to be constructed efficiently.
