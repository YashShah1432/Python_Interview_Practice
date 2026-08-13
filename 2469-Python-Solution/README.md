# LeetCode 2469 - Convert the Temperature

## Problem

Given a temperature in **Celsius**, convert it into:

* **Kelvin**
* **Fahrenheit**

Return the result as an array:

```text
[Kelvin, Fahrenheit]
```

The answers should be accurate to within `10⁻⁵` of the actual answer.

## Approach

We use the standard temperature conversion formulas.

### Celsius to Kelvin

```text
Kelvin = Celsius + 273.15
```

So in Python:

```python
celsius + 273.15
```

### Celsius to Fahrenheit

```text
Fahrenheit = Celsius × 1.8 + 32
```

So in Python:

```python
celsius * 1.80 + 32.00
```

We calculate both values and store them in the `ans` list.

For example:

```text
celsius = 36.50
```

Kelvin:

```text
36.50 + 273.15 = 309.65
```

Fahrenheit:

```text
36.50 × 1.80 + 32 = 97.70
```

Therefore:

```text
[309.65, 97.7]
```

## Python Concepts Used

* Lists
* `append()`
* Arithmetic operators
* `round()`
* `return` statement
* Function parameters

## Time Complexity

**O(1)**

Only two calculations are performed regardless of the input value.

## Space Complexity

**O(1)**

The result always contains exactly two values.

## Key Learning

This problem demonstrates how mathematical formulas can be directly implemented in Python.

The two important formulas are:

```text
Kelvin = Celsius + 273.15
Fahrenheit = Celsius × 1.8 + 32
```
