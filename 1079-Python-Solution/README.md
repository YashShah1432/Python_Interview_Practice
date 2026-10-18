# LeetCode 1079 - Letter Tile Possibilities

## Problem

Given a string `tiles` representing letter tiles, return the number of possible non-empty sequences that can be formed using the tiles. Each tile can be used at most once, and identical sequences are counted only once.

## Approach

1. Initialize an empty set `subsets` to store unique sequences.
2. Iterate through sequence lengths from `1` to `len(tiles)`.
3. Use `permutations(tiles, i)` to generate all possible ordered sequences of length `i`.
4. Join each permutation into a string and add it to the set. The set automatically removes duplicate sequences.
5. Return the number of unique sequences using `len(subsets)`.

```
subsets = set()for i in range(1, len(tiles) + 1):    for combo in permutations(tiles, i):        subsets.add("".join(combo))return len(subsets)
```

## Python Concepts Used

- Strings
- Sets for storing unique values
- Nested `for` loops
- `range()` and `len()`
- `permutations()` from the `itertools` module
- `join()` for combining characters into strings
- `add()` for inserting elements into a set

## Time Complexity

O(n × n!) in the worst case, where `n` is the length of `tiles`, assuming all characters are distinct. Generating and storing all permutations across sequence lengths dominates the runtime.

## Space Complexity

O(n × n!) in the worst case for storing all unique sequences in the set.

## Key Learning

`permutations()` generates ordered arrangements of elements, while a `set` removes duplicate sequences when tiles contain repeated letters. Starting from length `1` ensures that the empty sequence is not counted.
