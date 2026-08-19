# LeetCode 3190 - Find Minimum Operations to Make All Elements Divisible by Three

## Problem

Given an integer array `nums`, find the minimum number of operations needed to make every element divisible by `3`.

In one operation, you can increase or decrease an element by `1`.

## Approach

Iterate through each number and check its remainder when divided by `3`.

If the remainder is `1`, decrease the number by `1`:

```python
if num % 3 == 1:
    num -= 1
    count += 1
```

If the remainder is `2`, increase the number by `1`:

```python
elif num % 3 == 2:
    num += 1
    count += 1
```

Numbers with remainder `0` are already divisible by `3`, so no operation is needed.

Finally, return the total number of operations.

## Python Concepts Used

* Lists
* `for` loop
* Modulo operator `%`
* `if-elif` statements
* Variables
* Increment operator
* Arithmetic operations
* `return` statement

## Time Complexity

**O(n)**

The array is traversed once.

## Space Complexity

**O(1)**

Only the `count` variable is used.

## Key Learning

The key idea is using the **remainder when dividing by 3** to determine whether an element needs one operation. Any number with a remainder of `1` or `2` can be made divisible by `3` with exactly one operation.
