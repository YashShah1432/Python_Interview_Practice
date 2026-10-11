# LeetCode 1769 - Minimum Number of Operations to Move All Balls to Each Box

## Problem

Given a string `boxes` where `'1'` represents a box containing a ball and `'0'` represents an empty box, return an array where each element represents the minimum number of operations required to move all balls to the corresponding box.

## Approach

1. Initialize an empty list `answer` to store the operation counts.
2. Iterate through every box using index `i`.
3. Initialize `count = 0` for each target box.
4. Traverse every box again using index `j`.
5. Skip the current box when `i == j` or skip any empty box where `boxes[j] == "0"`.
6. For every other box containing a ball, add `abs(i - j)` to `count` to calculate the distance the ball must travel.
7. Append the total count to `answer` and return the list.

```
answer = []for i in range(len(boxes)):    count = 0    for j in range(len(boxes)):        if i == j or boxes[j] == "0":            continue        else:            count = count + abs(i - j)    answer.append(count)return answer
```

## Python Concepts Used

- Strings and indexing
- Nested `for` loops
- Conditional statements
- `continue`
- `abs()` for calculating absolute distance
- Lists and `append()`
- Accumulator variable

## Time Complexity

O(n²), where `n` is the length of `boxes`, because the inner loop traverses the entire string for every target box.

## Space Complexity

O(n) for storing the `answer` list.

## Key Learning

Nested loops can calculate the total distance from every ball to each target box. The `abs(i - j)` expression calculates the number of moves required to transfer a ball between two positions.
