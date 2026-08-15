# LeetCode 2011 - Final Value of Variable After Performing Operations

## Problem

Given an array `operations`, where each operation either increments or decrements a variable `X`, return the final value of `X`.

* `"++X"` and `"X++"` increase the value by `1`.
* `"--X"` and `"X--"` decrease the value by `1`.

The initial value of `X` is `0`.

## Approach

Initialize `result` to `0` and iterate through each operation.

If the operation is either `"++X"` or `"X++"`, add `1`; otherwise, subtract `1`.

```python
result += 1 if operation in ("++X", "X++") else -1
```

Finally, return the value of `result`.

## Python Concepts Used

* `for` loop
* Strings
* Tuple
* `in` operator
* Conditional expression
* Addition and subtraction
* `return` statement

## Time Complexity

**O(n)**

Each operation is processed exactly once.

## Space Complexity

**O(1)**

Only the `result` variable is used.

## Key Learning

The key idea is to simplify the four possible operations into two cases: **increment** or **decrement**. A Python conditional expression allows this to be handled concisely in a single line.
