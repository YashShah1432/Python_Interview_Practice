# LeetCode 3016 - Minimum Number of Pushes to Type Word II

## Problem

Given a string `word`, assign its characters to the keys of a phone keypad to minimize the total number of pushes required to type the word. Each key can hold up to eight characters, and characters used more frequently should require fewer pushes.

## Approach

1. Use `Counter(word)` to count the frequency of each character.
2. Sort the character-frequency pairs in descending order of frequency.
3. Count the position of each character in the sorted dictionary using `enumerate()`.
4. Calculate the push cost based on the character's position:
   - Indices `0–7`: one push per occurrence.
   - Indices `8–15`: two pushes per occurrence.
   - Indices `16–23`: three pushes per occurrence.
   - Indices `24` onward: four pushes per occurrence.
5. Add the weighted frequency of each character to `count`.
6. Return the total number of pushes.

```
collection = Counter(word)new_collection = dict(    sorted(collection.items(), key=lambda item: item[1], reverse=True))count = 0for index, (key, value) in enumerate(new_collection.items()):    if index <= 7:        count += collection[key]    elif index <= 15:        count += collection[key] * 2    elif index <= 23:        count += collection[key] * 3    else:        count += collection[key] * 4return count
```

## Python Concepts Used

- `Counter` from the `collections` module
- Dictionaries and frequency counting
- `sorted()` with a `lambda` function
- `reverse=True` for descending order
- `enumerate()` for tracking indices
- Dictionary iteration using `.items()`
- Conditional statements
- Accumulator variable

## Time Complexity

O(n + k log k), where `n` is the length of `word` and `k` is the number of distinct characters. Counting takes O(n), and sorting the distinct characters takes O(k log k).

## Space Complexity

O(k) for storing character frequencies and the sorted dictionary, where `k` is the number of distinct characters.

## Key Learning

Sorting characters by frequency ensures that the most frequent characters receive the lowest push costs. Using `Counter`, `sorted()`, and `enumerate()` makes it straightforward to calculate the total weighted push count.
