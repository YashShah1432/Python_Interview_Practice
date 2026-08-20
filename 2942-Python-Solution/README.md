# LeetCode 2942 - Find Words Containing Character

## Problem

Given an array of strings `words` and a character `x`, return the indices of the words that contain `x`.

## Approach

Iterate through each word and check whether removing `x` from the word changes it:

```python
if word != word.replace(x, ""):
```

If the word contains `x`, add its index to `result`.

The `count` variable keeps track of the current index:

```python
count += 1
result.append(count)
```

Finally, return the list of indices.

## Python Concepts Used

* Lists
* Strings
* `for` loop
* `replace()` method
* String comparison
* `append()`
* Counter variable
* `return` statement

## Time Complexity

**O(n × m)**

Where `n` is the number of words and `m` is the average length of a word.

## Space Complexity

**O(n)**

The `result` list stores the indices of matching words.

## Key Learning

The key idea is using the **`replace()` method to check whether a character exists in a string**. If removing the character changes the string, the character was present.
