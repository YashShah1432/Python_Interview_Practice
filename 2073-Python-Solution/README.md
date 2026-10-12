# LeetCode 2073 - Time Needed to Buy Tickets

## Problem

Given an array `tickets`, where `tickets[i]` represents the number of tickets person `i` wants to buy, and an index `k`, calculate the total time required for the person at index `k` to finish buying all their tickets. Each person buys one ticket per second, following the queue order.

## Approach

1. Initialize `total = 0` to track the time required.
2. Traverse the `tickets` array using index `i`.
3. For people standing before `k`, add the minimum of their ticket count and `tickets[k]`.
4. For people standing after `k`, add the minimum of their ticket count and `tickets[k] - 1`, since they get one fewer opportunity before person `k` finishes.
5. For the person at index `k`, add `tickets[k]` to the total.
6. Return `total`.

```
total = 0for i in range(len(tickets)):    if i < k:        total += tickets[i] if tickets[i] <= tickets[k] else tickets[k]    elif i > k:        total += tickets[i] if tickets[i] <= tickets[k] - 1 else tickets[k] - 1    else:        total += tickets[k]return total
```

## Python Concepts Used

- Lists and indexing
- `for` loops
- Conditional statements (`if`, `elif`, `else`)
- Ternary conditional expressions
- Accumulator variable
- `len()`

## Time Complexity

O(n), where `n` is the length of `tickets`, because the array is traversed once.

## Space Complexity

O(1) because only a constant amount of extra space is used.

## Key Learning

The number of turns each person gets depends on their position relative to `k`. People before `k` can buy up to `tickets[k]` tickets, while people after `k` can buy up to `tickets[k] - 1` tickets before the target person finishes.
