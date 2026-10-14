# LeetCode 4020 - Elevator Requests

## Problem

Given the number of floors `n` and a list of elevator floor requests, calculate the total time required to serve the requests in order, assuming the elevator starts at floor `0` and each floor transition takes one unit of time.

## Approach

1. Initialize `total_time` with `requests[0]`, representing the time taken to travel from floor `0` to the first requested floor.
2. Iterate through the remaining requests starting from index `1`.
3. Calculate the absolute difference between the current floor request and the previous floor request using `abs()`.
4. Add each floor difference to `total_time`.
5. Return the total time.

```
total_time = requests[0]for i in range(1, len(requests)):    total_time = total_time + abs(requests[i] - requests[i - 1])return total_time
```

## Python Concepts Used

- Lists and indexing
- `for` loops
- `range()`
- `len()`
- `abs()` for absolute differences
- Accumulator variable

## Time Complexity

O(n), where `n` is the number of requests, because each request is processed once.

## Space Complexity

O(1) because only a constant amount of extra space is used.

## Key Learning

The absolute difference between consecutive floor requests gives the distance traveled between them. Adding these distances, along with the initial travel from floor `0`, calculates the total elevator travel time.
