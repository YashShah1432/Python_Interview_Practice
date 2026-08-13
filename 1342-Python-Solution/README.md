# LeetCode 1342 - Number of Steps to Reduce a Number to Zero

## Problem

Given a non-negative integer `num`, return the number of steps required to reduce it to `0`.

At each step:

* If `num` is **even**, divide it by `2`.
* If `num` is **odd**, subtract `1`.

Continue until `num` becomes `0`.

## Approach

Initialize a counter to keep track of the number of steps:

```python
count = 0
```

Then continue performing operations while `num` is greater than `0`:

```python
while num > 0:
```

First, check whether the number is odd:

```python
if num % 2 == 1:
    num -= 1
    count += 1
```

If the number is odd, subtract `1` to make it even and count one step.

Then check whether the number is still greater than `0`:

```python
if num > 0:
    num /= 2
    count += 1
```

If it is greater than `0`, divide it by `2` and count another step.

Finally, return the total number of steps.

### Example

```text
num = 14
```

The operations are:

```text
14 → 7    divide by 2
7  → 6    subtract 1
6  → 3    divide by 2
3  → 2    subtract 1
2  → 1    divide by 2
1  → 0    subtract 1
```

Total:

```text
6 steps
```

## Python Concepts Used

* `while` loop
* `if` condition
* Modulo operator `%`
* Arithmetic operators
* Counter variable
* `return` statement

## Time Complexity

**O(log n)**

Division by `2` significantly reduces the value of `num` at every even step.

## Space Complexity

**O(1)**

Only the variables `num` and `count` are used.

## Key Learning

The important part of this problem is identifying whether the current number is **odd or even**:

```python
num % 2 == 1
```

If true, the number is odd and we subtract `1`.

If false, the number is even and we divide it by `2`.
