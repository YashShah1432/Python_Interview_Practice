# LeetCode 1688 - Count of Matches in Tournament

## Problem

Given `n` teams in a tournament, calculate the total number of matches played until exactly one team remains.

* If the number of teams is even, `n / 2` matches are played.
* If the number of teams is odd, `(n - 1) / 2` matches are played and one team advances directly.

## Approach

1. Initialize `matches` to `0`.
2. Continue while more than one team remains.
3. If `n` is even, add `n / 2` matches and reduce the teams to `n / 2`.
4. If `n` is odd, add `(n - 1) / 2` matches and update the teams to `(n - 1) / 2 + 1`.
5. Return the total number of matches.

```python
matches = 0

while n > 1:
    if n % 2 == 0:
        matches += n / 2
        n /= 2
    else:
        matches += (n - 1) / 2
        n = (n - 1) / 2 + 1

return int(matches)
```

## Python Concepts Used

* **While loop** – Continue the tournament until one team remains.
* **Modulo operator `%`** – Check whether the number of teams is even or odd.
* **Arithmetic operations** – Calculate matches and remaining teams.
* **Type conversion** – Convert the final result to an integer using `int()`.

## Time Complexity

**O(log n)** — The number of teams is reduced approximately by half after each round.

## Space Complexity

**O(1)** — Only a few variables are used.

## Key Learning

Tournament problems can often be solved by **simulating each round** and handling even and odd numbers of participants separately.
