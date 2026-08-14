# LeetCode 2413 - Smallest Even Multiple

## Problem

Given a positive integer `n`, return the smallest positive integer that is a multiple of both `2` and `n`.

## Approach

Check whether `n` is already even.

If `n` is even, then `n` itself is the smallest even multiple:

```text
n % 2 == 0 → return n
```

If `n` is odd, multiplying it by `2` produces the smallest even multiple:

```text
n % 2 != 0 → return n × 2
```

## Python Concepts Used

* `if-else` statements
* Modulo operator `%`
* Arithmetic multiplication
* `return` statement
* Function parameters

## Time Complexity

**O(1)**

Only one condition is checked.

## Space Complexity

**O(1)**

No additional data structures are used.

## Key Learning

The key idea is to use the **parity of the number**. An even number is already a multiple of `2`, while an odd number needs to be multiplied by `2` to become the smallest even multiple.
