# LeetCode 2391 - Minimum Amount of Time to Collect Garbage

## Problem

Given a list of garbage types in different houses and a travel time array between consecutive houses, calculate the minimum time required for three garbage trucks to collect all garbage. Each truck collects one type of garbage: metal (`M`), paper (`P`), or glass (`G`).

## Approach

1. Initialize variables `g`, `p`, and `m` to track the last house containing each garbage type, along with `total` to store the travel time.
2. Traverse the `garbage` list backward to find the last house containing glass (`G`).
3. Repeat the process to find the last house containing paper (`P`) and metal (`M`).
4. Sum the travel times from the first house up to each truck's last required house.
5. Concatenate all garbage strings and use `len()` to count the total collection time, since collecting each garbage unit takes one minute.
6. Return the sum of the travel and collection times.

```
n = len(garbage)g, p, m, total = 0, 0, 0, 0for i in range(n - 1, 0, -1):    if 'G' in garbage[i]:        g = i        breakfor i in range(n - 1, 0, -1):    if 'P' in garbage[i]:        p = i        breakfor i in range(n - 1, -1, -1):    if 'M' in garbage[i]:        m = i        breakfor i in range(g):    total += travel[i]for i in range(p):    total += travel[i]for i in range(m):    total += travel[i]return total + len("".join(garbage))
```

## Python Concepts Used

- Lists and indexing
- Reverse iteration using `range()`
- Membership operator `in`
- `break` statement
- Multiple variable assignment
- `for` loops
- Accumulator variable
- `join()` and `len()`

## Time Complexity

O(n + L), where `n` is the number of houses and `L` is the total number of garbage characters. The garbage list is traversed several times, and all garbage strings are concatenated once.

## Space Complexity

O(L) for the concatenated string created by `"".join(garbage)`.

## Key Learning

Finding the last house containing each garbage type helps determine how far each truck must travel. The total time is the sum of the travel distances for all three trucks and the time required to collect every piece of garbage.
