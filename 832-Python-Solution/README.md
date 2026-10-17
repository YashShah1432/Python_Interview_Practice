# LeetCode 832 - Flipping an Image

## Problem

Given a binary matrix `image`, flip each row horizontally and then invert every bit (`0` becomes `1` and `1` becomes `0`). Return the modified image.

## Approach

1. Initialize an empty list `answer` to store the modified rows.
2. Traverse each row of the matrix.
3. Iterate through every element in the current row and invert it:
   - If the value is `1`, change it to `0`.
   - Otherwise, change it to `1`.
4. Reverse the modified row using `image[i][::-1]`.
5. Append the reversed row to `answer`.
6. Return the final matrix.

```
answer = []for i in range(len(image)):    for j in range(len(image[i])):        image[i][j] = 0 if image[i][j] == 1 else 1    answer.append(image[i][::-1])return answer
```

## Python Concepts Used

- Nested lists and matrix traversal
- Nested `for` loops
- List indexing
- Conditional expressions
- List slicing (`[::-1]`) for reversing a row
- `append()`

## Time Complexity

O(m × n), where `m` is the number of rows and `n` is the number of columns, because every matrix element is inverted and each row is reversed.

## Space Complexity

O(m × n) for storing the modified rows in `answer`.

## Key Learning

A horizontal flip can be performed using list slicing with `[::-1]`, while bit inversion can be handled using a conditional expression. Performing these operations row by row transforms the binary matrix as required.
