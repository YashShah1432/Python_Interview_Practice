# LeetCode 3658 - GCD of Odd and Even Sums

## Problem

Given an integer `n`, calculate the sum of the first `n` even positive integers and the sum of the first `n` odd positive integers.

Return the **GCD** of these two sums.

## Approach

Use two loops to calculate the even and odd sums.

For even numbers:

```python id="7h9m2k"
for i in range(0, n*2, 2):
    even_sum += i
```

For odd numbers:

```python id="k3r6vp"
for i in range(1, n*2, 2):
    odd_sum += i
```

Then use `math.gcd()` to calculate the GCD of both sums:

```python id="p4w8qs"
return math.gcd(even_sum, odd_sum)
```

## Python Concepts Used

* `for` loop
* `range()` with step
* Variables
* Arithmetic operations
* `math.gcd()`
* `return` statement

## Time Complexity

**O(n)**

Both loops run `n` times.

## Space Complexity

**O(1)**

Only two variables are used to store the sums.

## Key Learning

The key idea is to **separate even and odd numbers, calculate their sums, and use `math.gcd()` to find their greatest common divisor**.
