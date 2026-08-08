# LeetCode 69 - Sqrt(x)

## Problem
Given a non-negative integer `x`, return the **integer square root** of `x`.

The integer square root is the largest integer `n` such that:

`n × n <= x`

Do not use built-in exponent or square-root functions.

## Approach
1. If `x` is `0` or `1`, return `x` directly.
2. Use **binary search** between `2` and `x // 2`.
3. Calculate the square of the middle value.
4. If `mid * mid == x`, return `mid`.
5. If `mid * mid < x`, search the right half.
6. If `mid * mid > x`, search the left half.
7. When the loop ends, `right` represents the largest integer whose square is less than or equal to `x`.

### Example

For:

```text
x = 8
```

The integer square root is:

```text
2
```

because:

```text
2 × 2 = 4 <= 8
3 × 3 = 9 > 8
```

Therefore, the answer is `2`.

## Python Concepts Used
- Binary Search
- `while` Loop
- Integer Division (`//`)
- Conditional Statements
- Variables and Comparison Operators

## Time Complexity
**O(log n)**

Binary search cuts the search range roughly in half during every iteration.

## Space Complexity
**O(1)**

Only a constant number of variables are used.
