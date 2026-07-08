# LeetCode 13 - Roman to Integer

## Problem

Given a Roman numeral, convert it to an integer.

Roman numerals are represented by seven different symbols:

| Symbol | Value |
| ------ | ----: |
| I      |     1 |
| V      |     5 |
| X      |    10 |
| L      |    50 |
| C      |   100 |
| D      |   500 |
| M      |  1000 |

Roman numerals are usually written from largest to smallest. However, when a smaller numeral appears before a larger numeral, it indicates subtraction.

Examples:

* `IV = 4`
* `IX = 9`
* `XL = 40`
* `XC = 90`
* `CD = 400`
* `CM = 900`

## Approach

1. Create a dictionary that maps each Roman numeral to its integer value.
2. Initialize a variable `total` to `0`.
3. Traverse the Roman numeral string from left to right.
4. Compare the current symbol with the next symbol:

   * If the current value is smaller than the next value, subtract it from `total`.
   * Otherwise, add it to `total`.
5. Return the final value stored in `total`.

## Python Concepts Used

* Dictionary (`dict`)
* String Traversal
* Conditional Statements (`if-else`)
* Dictionary Lookup
* Arithmetic Operations

## Time Complexity

**O(n)**

* The string is traversed once, where `n` is the length of the Roman numeral.

## Space Complexity

**O(1)**

* The dictionary contains a fixed number of Roman numeral mappings, so the extra space required is constant.
