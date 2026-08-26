# LeetCode 2657 - Find the Prefix Common Array of Two Arrays

## Problem

Given two integer arrays `A` and `B` that are permutations of the same elements, find the number of elements that are common between the prefixes of `A` and `B` at each index.

## Approach

For each index `i`, take the prefixes of both arrays:

```python
A[:i+1]
B[:i+1]
```

Convert them into sets and find their intersection:

```python
set(A[:i+1]) & set(B[:i+1])
```

The length of the intersection gives the number of common elements:

```python
len(list(set(A[:i+1]) & set(B[:i+1])))
```

Append this count to `result` for every index.

## Python Concepts Used

* Lists
* List slicing
* Sets
* Set intersection `&`
* `set()`
* `len()`
* `append()`
* `for` loop
* `range()`

## Time Complexity

**O(n²)**

For each index, prefixes are created and converted into sets.

## Space Complexity

**O(n)**

Temporary sets and the `result` list require additional space.

## Key Learning

The key idea is to **compare the prefixes of both arrays using set intersection**. The size of the intersection gives the number of common elements at each prefix.
