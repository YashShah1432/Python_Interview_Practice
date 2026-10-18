# LeetCode 2610 - Convert an Array Into a 2D Array With Conditions

## Problem

Given an integer array `nums`, convert it into a 2D array such that each row contains distinct integers, every element from `nums` appears in the 2D array, and the number of rows is minimized.

## Approach

1. Initialize an empty list `result` to store the rows and a `Counter` to track the frequency of each number.
2. Traverse each number in `nums`.
3. Use `counts[num]` as the row index for the current occurrence of that number.
4. If the row index equals `len(result)`, create a new empty row.
5. Append the number to the selected row and increment its count.
6. Return the resulting 2D array.

```
result = []counts = Counter()for num in nums:    row_index = counts[num]    if row_index == len(result):        result.append([])    result[row_index].append(num)    counts[num] += 1return result
```

## Python Concepts Used

- Lists and nested lists
- `Counter` from the `collections` module
- `for` loops
- Dictionary-style frequency counting
- List indexing
- Conditional statements
- `append()`

## Time Complexity

O(n), where `n` is the length of `nums`, assuming `Counter` operations take O(1) time on average.

## Space Complexity

O(n) for storing all elements in the resulting 2D array and tracking their frequencies.

## Key Learning

The frequency of each number determines the row where its next occurrence should be placed. This approach ensures that duplicate values appear in different rows while creating only as many rows as necessary.
