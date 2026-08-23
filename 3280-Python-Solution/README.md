# LeetCode 3280 - Convert Date to Binary

## Problem

Given a date in the format `YYYY-MM-DD`, convert each part of the date into its **binary representation** and return the result in the same format.

## Approach

Split the date into its three parts using `-`:

```python
arr = date.split("-")
```

Convert each part into an integer and then into binary:

```python
binary = bin(int(num))
```

Remove the `0b` prefix from the binary representation:

```python
result.append(binary[2:])
```

Finally, join the three binary values using `-`:

```python
return "-".join(result)
```

## Python Concepts Used

* Strings
* `split()`
* Lists
* `for` loop
* `int()`
* `bin()`
* String slicing
* `append()`
* `join()`
* `return` statement

## Time Complexity

**O(n)**

The date contains a fixed number of characters, and each part is processed once.

## Space Complexity

**O(n)**

Additional space is used for the split date and result list.

## Key Learning

The key idea is to **split the date into separate parts, convert each number to binary using `bin()`, remove the `0b` prefix, and join the results back together**.
