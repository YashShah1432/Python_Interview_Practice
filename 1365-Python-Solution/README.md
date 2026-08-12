# LeetCode 1365 - How Many Numbers Are Smaller Than the Current Number

## Problem

Given an integer array `nums`, for each element `nums[i]`, find the number of elements that are **smaller than `nums[i]`**.

Return the result as an array where `result[i]` represents the number of elements in `nums` that are smaller than `nums[i]`.

## Approach

For every element in the array, compare it with **every other element**.

First, initialize an empty `result` list:

```python
result = []
```

Then use a nested loop:

```python
for i in range(0, len(nums)):
    count = 0

    for j in range(0, len(nums)):
        if nums[i] > nums[j]:
            count += 1

    result.append(count)
```

The outer loop selects the current number:

```text
nums[i]
```

The inner loop compares that number with every element:

```text
nums[j]
```

Whenever:

```text
nums[i] > nums[j]
```

the current number has found one smaller element, so `count` is increased by `1`.

Finally, append the count to `result`.

For example:

```text
nums = [8, 1, 2, 2, 3]
```

For `8`:

```text
8 > 1  → count = 1
8 > 2  → count = 2
8 > 2  → count = 3
8 > 3  → count = 4
```

So:

```text
8 → 4
```

For `1`:

```text
1 > anything → False
```

So:

```text
1 → 0
```

For `2`:

```text
2 > 1 → count = 1
```

So:

```text
2 → 1
```

The final result is:

```text
[4, 0, 1, 1, 3]
```

### How the nested loop works

```python
for i in range(0, len(nums)):
```

Selects each number one by one.

```python
for j in range(0, len(nums)):
```

Compares that number with every element in the array.

```python
if nums[i] > nums[j]:
```

Checks whether the current number is greater than the other number.

```python
count += 1
```

Increases the count whenever a smaller number is found.

## Python Concepts Used

* Nested `for` loops
* `range()`
* Lists
* Array indexing
* Comparison operators
* Counter variable
* `append()`

## Time Complexity

**O(n²)**

For every element, we compare it with every other element using a nested loop.

## Space Complexity

**O(n)**

The `result` array stores one value for every element in `nums`.
