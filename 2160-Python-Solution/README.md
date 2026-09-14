# LeetCode 2160 - Minimum Sum of Four Digit Number After Splitting Digits

## Problem

Given a four-digit integer `num`, split its digits into two two-digit numbers such that their sum is minimized.

## Approach

1. Convert the number into a string and extract its digits.
2. Sort the digits in ascending order.
3. Form two numbers by pairing the smallest digit with the third-smallest and the second-smallest with the largest.
4. Convert them back to integers and return their sum.

```python
digits = sorted(list(str(num)))

new1 = int(digits[0] + digits[2])
new2 = int(digits[1] + digits[3])

return new1 + new2
```

Sorting the digits ensures that the smaller digits are placed in the tens positions, minimizing the overall sum.

## Python Concepts Used

* **`str()`** – Convert the integer into a string.
* **`list()`** – Convert the string into a list of digits.
* **`sorted()`** – Arrange digits in ascending order.
* **String concatenation** – Combine digits to form two-digit numbers.
* **`int()`** – Convert the constructed strings back into integers.
* **List indexing** – Access individual sorted digits.

## Time Complexity

**O(1)** — The input always contains exactly four digits, so sorting takes constant time.

## Space Complexity

**O(1)** — Only a fixed number of digits and variables are stored.

## Key Learning

Sorting the digits and placing the **smallest digits in the tens positions** is the key to minimizing the sum of the two resulting numbers.
