# LeetCode 739 - Daily Temperatures

## Problem

Given an array of daily temperatures, return an array where each element represents the number of days you must wait until a warmer temperature. If no warmer temperature exists, the value should be `0`.

## Approach

1. Calculate the length of `temperatures` and initialize `answer` with zeros.
2. Create an empty stack to store the indices of days whose warmer temperatures have not yet been found.
3. Traverse the temperatures using `current_day`.
4. While the stack is not empty and the current temperature is warmer than the temperature at the top index of the stack:
   - Pop the previous day's index.
   - Calculate the difference between the current day and the previous day.
   - Store this difference in `answer`.
5. Push the current day's index onto the stack.
6. Return the `answer` array.

```
n = len(temperatures)answer = [0] * nstack = []for current_day in range(n):    current_temp = temperatures[current_day]    while stack and current_temp > temperatures[stack[-1]]:        previous_day = stack.pop()        answer[previous_day] = current_day - previous_day    stack.append(current_day)return answer
```

## Python Concepts Used

- Lists
- List initialization using `[0] * n`
- Stack operations using `append()` and `pop()`
- `for` and `while` loops
- List indexing
- Conditional expressions
- Monotonic stack

## Time Complexity

O(n), where `n` is the number of temperatures. Each index is pushed onto and popped from the stack at most once.

## Space Complexity

O(n) for the `answer` array and the stack in the worst case.

## Key Learning

A monotonic stack helps solve problems involving the next greater element efficiently. By storing indices and resolving them whenever a warmer temperature appears, the solution avoids repeatedly scanning future days for each temperature.
