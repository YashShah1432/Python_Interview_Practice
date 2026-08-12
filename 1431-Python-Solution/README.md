# LeetCode 1431 - Kids With the Greatest Number of Candies

## Problem

Given an integer array `candies`, where `candies[i]` represents the number of candies the `i`th child has, and an integer `extraCandies`, determine whether each child can have the **greatest number of candies** after receiving all the extra candies.

Return a Boolean array where each value is:

```text
True  → The child can have the greatest number of candies.
False → The child cannot have the greatest number of candies.
```

## Approach

First, find the highest number of candies currently held by any child:

```python
highest = max(candies)
```

Then iterate through every child and add `extraCandies` to their current number of candies.

For each child, check whether their new candy count is greater than or equal to the current highest:

```python
candies[i] += extraCandies

if candies[i] >= highest:
    result.append(bool(True))
else:
    result.append(bool(False))
```

If the condition is satisfied, append `True`; otherwise, append `False`.

For example:

```text
candies = [2, 3, 5, 1, 3]
extraCandies = 3
```

The highest number of candies is:

```text
5
```

After adding the extra candies:

```text
2 + 3 = 5  → True
3 + 3 = 6  → True
5 + 3 = 8  → True
1 + 3 = 4  → False
3 + 3 = 6  → True
```

Therefore, the result is:

```text
[True, True, True, False, True]
```

### How the loop works

The loop goes through every index:

```python
for i in range(0, len(candies)):
```

For each index, the child's candies are increased by `extraCandies`:

```python
candies[i] += extraCandies
```

Then we compare the new value with `highest`.

If:

```text
new candies >= highest
```

the child can have the greatest number of candies.

Otherwise, they cannot.

## Python Concepts Used

* `for` loop
* `range()`
* `max()`
* Lists
* Array indexing
* Arithmetic operators
* Conditional statements
* Boolean values
* `append()`

## Time Complexity

**O(n)**

The solution finds the maximum value in `O(n)` and then iterates through the array once.

## Space Complexity

**O(n)**

The `result` array stores one Boolean value for every child.
