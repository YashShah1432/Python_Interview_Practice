# LeetCode 3838 - Map Word Weights

## Problem

Given an array of words and an array of letter weights, calculate the weight of each word and map the resulting value to a letter.

## Approach

For each word, calculate its total weight by adding the corresponding weight of each character:

```python
weight += weights[ord(char) - ord('a')]
```

Convert the total weight into a value from `0` to `25` using modulo `26`:

```python
mod = weight % 26
```

Then map the value to a letter using:

```python
letter = chr(ord('z') - mod)
```

Append each resulting letter to `mod_arr` and return the final string.

## Python Concepts Used

* Lists
* Strings
* Nested `for` loops
* `ord()`
* `chr()`
* Modulo operator `%`
* String concatenation
* Array indexing
* `append()` / string accumulation
* `return` statement

## Time Complexity

**O(n × m)**

Where `n` is the number of words and `m` is the average length of each word.

## Space Complexity

**O(n)**

The resulting string contains one character for each word.

## Key Learning

The key idea is converting characters into **indices using `ord()`**, using those indices to access their weights, and then mapping the weighted result back to a letter using `chr()`.
