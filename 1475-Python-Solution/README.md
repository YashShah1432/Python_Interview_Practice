# LeetCode 1475 - Final Prices With a Special Discount in a Shop

## Problem

Given an integer array `prices`, for each item find the first price to its right that is **less than or equal to** its current price.

Apply that price as a discount. If no such price exists, keep the original price.

## Approach

Iterate through each price and search the elements to its right:

```python
for j in range(i + 1, len(prices)):
```

When the first price satisfying:

```python
prices[j] <= prices[i]
```

is found, subtract it from the current price and add the discounted price to `answer`.

A `discount_applied` flag is used to determine whether a valid discount was found. If no discount is found, the original price is added.

## Python Concepts Used

* Nested `for` loops
* Lists
* List indexing
* `range()`
* Boolean variables
* `break` statement
* `append()`
* Arithmetic operations
* Conditional statements

## Time Complexity

**O(n²)**

For each price, the solution may scan all elements to its right.

## Space Complexity

**O(n)**

The `answer` list stores the final price for every item.

## Key Learning

The key idea is to find the **first valid discount to the right** and immediately stop searching using `break`. This avoids unnecessary comparisons once the required discount has been found.
