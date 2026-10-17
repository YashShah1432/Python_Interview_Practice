# LeetCode 3551 - Minimum Swaps to Sort by Digit Sum

## Problem

Given an integer array `nums`, sort the elements by their digit sum in ascending order. If two elements have the same digit sum, sort them by their numerical value in ascending order. Return the minimum number of swaps required to arrange the array in this order.

## Approach

1. Calculate the digit sum of each number using a `while` loop and store `[digit_sum, number, original_index]` in `digit_sum`.
2. Sort `digit_sum` lexicographically, which sorts by digit sum first and number second.
3. Create a `visited` list to track elements that have already been processed.
4. Traverse the sorted list and skip elements that are already visited or are already in their correct position.
5. For each remaining element, follow its original indices to identify a cycle and mark its elements as visited.
6. Add the cycle length minus one to `swaps`, since a cycle of length \\(k\\) requires \\(k-1\\) swaps.
7. Return the total number of swaps.

```
digit_sum = []for i in range(n):    num = nums[i]    temp = num    total = 0    while temp > 0:        total += temp % 10        temp //= 10    digit_sum.append([total, num, i])digit_sum.sort()visited = [False] * nswaps = 0for i in range(n):    if visited[i] or digit_sum[i][2] == i:        continue    curr_idx = i    while not visited[curr_idx]:        visited[curr_idx] = True        curr_idx = digit_sum[curr_idx][2]        swaps += 1    swaps -= 1return swaps
```

## Python Concepts Used

- Lists and nested lists
- `while` loops
- Modulo operator (`%`) for extracting digits
- Floor division (`//`) for removing digits
- `sort()` for lexicographical sorting
- Boolean lists for tracking visited elements
- Cycle detection
- Indexing

## Time Complexity

O(n log n), where `n` is the length of `nums`. Sorting takes O(n log n), while calculating digit sums and processing cycles take O(n) time, assuming a bounded number of digits per integer.

## Space Complexity

O(n) for storing digit sums, original indices, and visited status.

## Key Learning

Cycle detection helps calculate the minimum number of swaps required to transform an array into a target order. Each cycle of length \\(k\\) requires exactly \\(k-1\\) swaps, and storing original indices makes it possible to identify these cycles after sorting.
