# LeetCode 2974 - Minimum Number Game

## Problem

Given an integer array `nums` containing an even number of elements, Alice and Bob play a game where:

- Alice removes the smallest element from `nums`.
- Bob removes the next smallest element.
- Bob appends his removed element to the result array first.
- Alice then appends her removed element.

Return the resulting array after all elements have been removed.

## Approach

1. Sort `nums` in ascending order using `sort()`.
2. Extract elements at even indices using `nums[::2]` and store them in `alice`.
3. Extract elements at odd indices using `nums[1::2]` and store them in `bob`.
4. Initialize an empty list `arr`.
5. Iterate through both lists, appending Bob's element first, followed by Alice's element.
6. Return the final rearranged array.

```
nums.sort()alice = nums[::2]bob = nums[1::2]arr = []for i in range(len(alice)):    arr.append(bob[i])    arr.append(alice[i])return arr
```

## Python Concepts Used

- Lists
- `sort()` for sorting elements
- List slicing (`[::2]` and `[1::2]`)
- `for` loops
- `range()` and `len()`
- List indexing
- `append()` for adding elements

## Time Complexity

O(n log n), where `n` is the length of `nums`.

- Sorting takes O(n log n).
- List slicing takes O(n).
- Constructing the result takes O(n).

Therefore, the overall time complexity is O(n log n).

## Space Complexity

O(n) for storing the `alice`, `bob`, and `arr` lists.

## Key Learning

List slicing provides an efficient way to separate elements at even and odd indices. After sorting the array, pairing consecutive elements and placing Bob's element before Alice's produces the required result without explicitly simulating each removal.
