# LeetCode 3541 - Find Most Frequent Vowel and Consonant

## Problem

Given a string `s`, find the highest frequency among the **vowels** and the highest frequency among the **consonants**, then return their sum.

## Approach

Use `Counter` to count the frequency of each character:

```python
char = Counter(s)
```

Create two lists to store vowel and consonant frequencies:

```python
vowel = [0]
consonent = [0]
```

Separate the characters into vowels and consonants:

```python
if key == 'a' or key == 'e' or key == 'i' or key == 'o' or key == 'u':
    vowel.append(count)
else:
    consonent.append(count)
```

Find the maximum frequency from both lists and add them:

```python
return max(vowel) + max(consonent)
```

## Python Concepts Used

* Strings
* `Counter`
* Lists
* `for` loop
* `if-else` statements
* `items()`
* `append()`
* `max()`
* `return` statement

## Time Complexity

**O(n)**

The string is traversed to count character frequencies.

## Space Complexity

**O(n)**

The `Counter` stores the frequency of distinct characters.

## Key Learning

The key idea is to **count character frequencies using `Counter`**, separate vowels and consonants, find the maximum frequency in each group, and add them together.
