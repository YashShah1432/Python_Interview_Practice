# LeetCode 2114 - Maximum Number of Words Found in Sentences

## Problem

Given an array of sentences, find the **maximum number of words** present in any single sentence.

## Approach

1. Iterate through each sentence.
2. Use `split()` to separate the sentence into individual words.
3. Count the words using `len()`.
4. Use `max()` to find the largest word count.

```python
return max(len(sentence.split()) for sentence in sentences)
```

## Python Concepts Used

* **`split()`** – Splits a sentence into a list of words.
* **`len()`** – Counts the number of words.
* **Generator expression** – Calculates word counts efficiently.
* **`max()`** – Finds the maximum word count.

## Time Complexity

**O(n × m)** — Where `n` is the number of sentences and `m` is the average number of words in a sentence.

## Space Complexity

**O(m)** — `split()` creates a list of words for the sentence being processed.

## Key Learning

Python built-in functions like `split()`, `len()`, and `max()` can be combined with a **generator expression** to solve simple aggregation problems concisely.
