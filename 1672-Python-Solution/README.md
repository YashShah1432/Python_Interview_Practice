# LeetCode 1672 - Richest Customer Wealth

## Problem
Given a 2D array `accounts`, where each row represents a customer and each value represents the amount of money they have in a bank account, find the **maximum wealth** among all customers.

A customer's wealth is the sum of all the money in their accounts.

## Approach
1. Create an empty list `result` to store each customer's total wealth.
2. Iterate through each customer's accounts.
3. Calculate the total money for that customer using a nested loop.
4. Store the calculated wealth in `result`.
5. Use `max()` to find and return the highest customer wealth.

### Example

For:

```text
accounts = [[1,2,3], [3,2,1]]
```

Customer wealth:

```text
1 + 2 + 3 = 6
3 + 2 + 1 = 6
```

Therefore:

```text
Maximum Wealth = 6
```

## Python Concepts Used
- Nested `for` Loops
- Lists
- Accumulator Variable
- `append()`
- `max()`
- 2D Array Traversal

## Time Complexity
**O(n × m)**

Where:
- `n` = number of customers
- `m` = number of accounts per customer

Every account value is visited once.

## Space Complexity
**O(n)**

The `result` list stores the total wealth of each customer.
