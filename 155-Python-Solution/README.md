# LeetCode 155 - Min Stack

## Problem

Design a stack that supports `push`, `pop`, `top`, and retrieving the minimum element in constant time.

## Approach

1. Use two stacks:
   - `st` stores all stack elements.
   - `min_stack` stores the minimum values encountered.
2. During `push`, add the value to `min_stack` if it is smaller than or equal to the current minimum.
3. During `pop`, if the removed value is the current minimum, remove it from `min_stack` as well.
4. `top()` returns the last element of `st`.
5. `getMin()` returns the last element of `min_stack`.

```python id="h2k7qm"
if not self.min_stack or value <= self.min_stack[-1]:
    self.min_stack.append(value)

self.st.append(value)
```

## Python Concepts Used

- Classes and objects
- `__init__()` constructor
- Instance variables
- Lists as stacks
- `append()`
- `pop()`
- Negative indexing
- Conditional statements
- Type hints

## Time Complexity

**O(1)** for `push`, `pop`, `top`, and `getMin`.

## Space Complexity

**O(n)** for storing elements in the two stacks.

## Key Learning

Using a separate `min_stack` allows the minimum element to be retrieved directly without searching through the entire stack. This makes `getMin()` an **O(1)** operation.
