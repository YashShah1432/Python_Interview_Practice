# LeetCode 1684 - Count the Number of Consistent Strings

## Problem

Given a string `allowed` and an array of strings `words`, count how many words contain **only characters that are present in `allowed`**.

## Approach

Use `Counter` to store the characters present in `allowed`:

```python
dict_allowed = Counter(allowed)
```

For each word, create a frequency dictionary:

```python
dict_word = Counter(word)
```

Check every character in the word. If a character is not present in `allowed`, mark the word as inconsistent:

```python
if key not in dict_allowed:
    isConsist = False
    break
```

If the word is consistent, increase the count:

```python
if isConsist:
    count += 1
```

Finally, return the total count.

## Python Concepts Used

* Strings
* Lists
* `Counter`
* Dictionaries
* Nested `for` loops
* `if` statements
* `break`
* `append()` / counter variable
* `return` statement

## Time Complexity

**O(n × m)**

Where `n` is the number of words and `m` is the average length of each word.

## Space Complexity

**O(m)**

Additional space is used by the character frequency dictionaries.

## Key Learning

The key idea is to **check every unique character of each word against the allowed characters** and count the words that contain no invalid characters.
