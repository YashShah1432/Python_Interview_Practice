# LeetCode 121 - Best Time to Buy and Sell Stock

## Problem

Given an array `prices` where `prices[i]` represents the price of a stock on the `i`th day, find the **maximum profit** that can be achieved by buying on one day and selling on a later day.

If no profit can be made, return `0`.

## Approach

Maintain two variables:

```python
min_price = float('inf')
max_profit = 0
```

`min_price` stores the **lowest stock price seen so far**, while `max_profit` stores the maximum profit found.

For every price:

* If the current price is lower than `min_price`, update `min_price`.
* Otherwise, calculate the potential profit:

```python
price - min_price
```

If this profit is greater than `max_profit`, update it.

This ensures that we always buy at the lowest price seen before the current selling day.

## Python Concepts Used

* `for` loop
* `if-elif` statements
* `float('inf')`
* Variables
* Arithmetic operations
* Comparison operators
* `return` statement

## Time Complexity

**O(n)**

The array is traversed exactly once.

## Space Complexity

**O(1)**

Only two variables are used regardless of the input size.

## Key Learning

The key idea is to keep track of the **minimum price seen so far** and calculate the best possible profit at each price. This avoids checking every possible buy-sell pair and reduces the solution from **O(n²)** to **O(n)**.
