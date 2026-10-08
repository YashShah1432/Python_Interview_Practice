# LeetCode 150 - Evaluate Reverse Polish Notation

## Problem

Given a list of tokens representing an arithmetic expression in Reverse Polish Notation (RPN), evaluate the expression and return the resulting integer.

## Approach

1. Use a stack `s` to store numbers.
2. Create a dictionary `operator` that maps each arithmetic operator to its corresponding operation using lambda functions.
3. Traverse each token:
   - If it is a number, convert it to an integer and push it onto the stack.
   - If it is an operator, pop the top two values from the stack.
4. Apply the operator while maintaining the correct operand order.
5. Push the calculated result back onto the stack.
6. Return the final value from the stack.

```python
s = []

operator = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: int(a / b)
}

for token in tokens:
    if token not in ['+', '-', '*', '/']:
        s.append(int(token))
    else:
        first = s.pop()
        second = s.pop()
        result = operator[token](second, first)
        s.append(result)

return s[0]
```

## Python Concepts Used

- Lists as stacks
- `append()` and `pop()`
- Dictionaries
- Lambda functions
- String-to-integer conversion using `int()`
- `for` loops
- Conditional statements
- Dictionary lookup

## Time Complexity

**O(n)**, where `n` is the number of tokens.

## Space Complexity

**O(n)** for the stack in the worst case.

## Key Learning

Reverse Polish Notation can be efficiently evaluated using a stack. When an operator is encountered, the last two numbers are popped, the operation is performed in the correct order, and the result is pushed back onto the stack.
