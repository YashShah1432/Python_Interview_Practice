# LeetCode 682 - Baseball Game

## Problem

Given a list of operations representing scores in a baseball game, calculate the total score after processing all operations.

## Approach

1. Use a list `stack` to store valid scores.
2. Traverse each operation:
   - `"+"` → add the previous two scores and push the result.
   - `"D"` → double the previous score and push it.
   - `"C"` → remove the previous score using `pop()`.
   - Otherwise, convert the operation to an integer and push it.
3. Return the sum of all scores in the stack.

```python id="4h9x2p"
stack = []

for ops in operations:
    if ops == "+":
        stack.append(stack[-1] + stack[-2])
    elif ops == "D":
        stack.append(stack[-1] * 2)
    elif ops == "C":
        stack.pop()
    else:
        stack.append(int(ops))

return sum(stack)
```

## Python Concepts Used

- Lists
- Stack implementation
- `append()`
- `pop()`
- Negative indexing
- `int()` conversion
- `sum()`
- `for` loops
- Conditional statements

## Time Complexity

**O(n)**, where `n` is the number of operations.

## Space Complexity

**O(n)** in the worst case for storing the scores in the stack.

## Key Learning

A stack is useful when operations depend on the most recently added elements. Using `append()` and `pop()` makes it straightforward to implement score operations such as cancellation, doubling, and calculating the sum of the previous two scores.
