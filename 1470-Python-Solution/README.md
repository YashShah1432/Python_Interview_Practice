# LeetCode 1470 - Shuffle the Array

## Problem
Given an array `nums` containing `2n` elements in the format:

```text
[x1, x2, ..., xn, y1, y2, ..., yn]
```

Return the array in the shuffled format:

```text
[x1, y1, x2, y2, ..., xn, yn]
```

## Approach

The original array contains two halves:

```text
[x1, x2, x3, ..., xn]
[y1, y2, y3, ..., yn]
```

We need to take one element alternately from each half.

For example:

```text
nums = [2, 5, 1, 3, 4, 7]
n = 3
```

The two halves are:

```text
First half  → [2, 5, 1]
Second half → [3, 4, 7]
```

We want:

```text
[2, 3, 5, 4, 1, 7]
```

### How the loop works

When `i` is even:

```python
if i % 2 == 0:
    result.append(nums[i // 2])
```

We take an element from the **first half**.

When `i` is odd:

```python
else:
    result.append(nums[n + (i // 2)])
```

We take the corresponding element from the **second half**.

So the indexes are:

```text
i = 0 → nums[0] → x1
i = 1 → nums[n] → y1
i = 2 → nums[1] → x2
i = 3 → nums[n+1] → y2
...
```

This produces:

```text
[x1, y1, x2, y2, ..., xn, yn]
```

## Python Concepts Used

- `for` loop
- `range()`
- Modulo operator `%`
- Integer division `//`
- Lists
- `append()`
- Array indexing

## Time Complexity

**O(n)**

Every element is visited exactly once.

## Space Complexity

**O(n)**

The `result` array contains `2n` elements.
