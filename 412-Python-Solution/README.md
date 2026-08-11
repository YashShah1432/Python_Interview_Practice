# LeetCode 412 - Fizz Buzz

## Problem
Given an integer `n`, return an array containing the numbers from `1` to `n`, following these rules:

- If the number is divisible by both `3` and `5`, return `"FizzBuzz"`.
- If the number is divisible by `3`, return `"Fizz"`.
- If the number is divisible by `5`, return `"Buzz"`.
- Otherwise, return the number as a string.

## Approach
1. Create an empty list `answer`.
2. Loop from `1` through `n`.
3. Check whether the current number is divisible by both `3` and `5`.
4. If not, check whether it is divisible by `3`.
5. Then check whether it is divisible by `5`.
6. If none of the conditions are true, convert the number to a string and add it to the list.
7. Return the final list.

### Example

For:

```text
n = 5
```

The output is:

```text
["1", "2", "Fizz", "4", "Buzz"]
```

For:

```text
n = 15
```

The last few values are:

```text
["11", "Fizz", "13", "14", "FizzBuzz"]
```

## Python Concepts Used
- `for` loop
- `range()`
- Modulo operator `%`
- `if / elif / else`
- Lists
- `append()`
- `str()`

## Time Complexity
**O(n)**

Every number from `1` to `n` is processed exactly once.

## Space Complexity
**O(n)**

The `answer` list contains `n` elements.
