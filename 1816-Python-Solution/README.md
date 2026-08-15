# LeetCode 1816 - Truncate Sentence

## Problem

Given a sentence `s` consisting of words separated by single spaces and an integer `k`, return the sentence containing only the **first `k` words**.

## Approach

Split the sentence into individual words using `split()` and take the first `k` words:

```python
new_str = s.split()[:k]
```

Then use `" ".join()` to combine those words back into a sentence:

```python
return " ".join(new_str)
```

> Your code has one small correction: `split(s)` should be `s.split()` because `split()` is a string method.

## Python Concepts Used

* Strings
* `split()` method
* List slicing `[:k]`
* `join()` method
* `return` statement
* Function parameters

## Time Complexity

**O(n)**

The sentence is split and reconstructed once.

## Space Complexity

**O(n)**

The split words and resulting string require additional space.

## Key Learning

The key idea is to use **`split()` to convert a sentence into a list of words**, use slicing to select the first `k` words, and then use **`join()` to reconstruct the sentence**.
