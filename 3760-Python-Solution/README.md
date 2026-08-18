# LeetCode 3760 - Maximum Distinct Elements After Operations

## Problem

Given a string `s`, find the number of **distinct characters** present in the string.

## Approach

Iterate through the string and store each character in a list:

```python
result.append(char)
```

Then convert the list into a set using:

```python
set(result)
```

A set contains only unique characters, so its length gives the number of distinct characters:

```python
return len(set(result))
```

## Python Concepts Used

* Strings
* Lists
* `for` loop
* `append()`
* Sets
* `set()`
* `len()`
* `return` statement

## Time Complexity

**O(n)**

The string is traversed once, and the set operation takes O(n) average time.

## Space Complexity

**O(n)**

The `result` list and set can store up to `n` characters.

## Key Learning

The key idea is using a **set to remove duplicate characters** and then finding its length to determine the number of distinct characters.
