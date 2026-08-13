# LeetCode 1528 - Shuffle String

## Problem

Given a string `s` and an integer array `indices`, the character at position `i` in `s` should be moved to position `indices[i]` in the shuffled string.

Return the resulting shuffled string.

## Approach

First, create an empty result array with the same length as the string:

```python
result = [''] * len(s)
```

This gives us an array with enough positions to place every character.

For example:

```text
s = "abc"
```

Initially:

```text
result = ["", "", ""]
```

Then iterate through every character in the string:

```python
for i in range(0, len(s)):
```

For each character, use `indices[i]` to determine its correct position:

```python
result[indices[i]] = s[i]
```

For example:

```text
s       = "abc"
indices = [2, 0, 1]
```

The characters are placed as:

```text
'a' → result[2]
'b' → result[0]
'c' → result[1]
```

So:

```text
result = ["b", "c", "a"]
```

Finally, convert the list into a string:

```python
return ''.join(result)
```

The final answer is:

```text
"bca"
```

## Python Concepts Used

* Strings
* Lists
* Array indexing
* `len()`
* `range()`
* `join()`
* List initialization
* `for` loop

## Time Complexity

**O(n)**

We iterate through the string once and then use `join()` to create the final string.

## Space Complexity

**O(n)**

The `result` list stores `n` characters.

## Key Learning

This problem demonstrates how an **index array can be used to rearrange elements**.

Instead of trying to swap characters repeatedly, we directly place each character at its required position:

```python
result[indices[i]] = s[i]
```

This makes the solution simple and efficient.
