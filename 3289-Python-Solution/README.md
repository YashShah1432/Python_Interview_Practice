# LeetCode 3289 - The Two Sneaky Numbers of Digitville

## Problem

Given an integer array `nums`, find the two numbers that appear **twice** in the array.

Return the numbers that have a frequency of exactly `2`.

## Approach

Use `Counter` to count how many times each number appears:

```python
dict_num = Counter(str(num) for num in nums)
```

Iterate through the frequency dictionary:

```python
for key, count in dict_num.items():
```

If a number appears exactly twice, add it to `result`:

```python
if count == 2:
    result.append(int(key))
```

Finally, return the result.

## Python Concepts Used

* Lists
* `Counter`
* Generator expressions
* `for` loop
* Dictionaries
* `items()`
* `append()`
* `int()`
* `return` statement

## Time Complexity

**O(n)**

The array is traversed to count the frequency of each number.

## Space Complexity

**O(n)**

The `Counter` can store the frequency of each distinct number.

## Key Learning

The key idea is using **`Counter` to count the frequency of each number** and selecting the numbers whose frequency is exactly `2`.
