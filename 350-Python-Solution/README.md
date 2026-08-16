# LeetCode 350 - Intersection of Two Arrays II

## Problem

Given two integer arrays `nums1` and `nums2`, return their intersection where each element may appear in the result as many times as it appears in both arrays.

## Approach

Use nested loops to compare every element of `nums1` with the elements of `nums2`.

When a match is found:

* Add the matching element to `result`.
* Remove that element from `nums2` so it cannot be matched again.
* Use `break` to move to the next element of `nums1`.

```python
if nums1[i] == nums2[j]:
    result.append(nums1[i])
    nums2.remove(nums2[j])
    break
```

Removing the matched element ensures that duplicate elements are handled according to their frequency in both arrays.

## Python Concepts Used

* Nested `for` loops
* Lists
* List indexing
* `remove()` method
* `append()` method
* `break` statement
* Comparison operators

## Time Complexity

**O(n × m)**

The nested loops compare elements from both arrays. Additionally, `remove()` can take O(m) time.

## Space Complexity

**O(n)**

The `result` list can contain up to `n` elements.

## Key Learning

The key idea is to **remove a matched element from `nums2`** so that the same occurrence cannot be used more than once. This allows the solution to correctly handle duplicate elements.
