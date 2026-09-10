# LeetCode 1415 - The k-th Lexicographical String of All Happy Strings of Length n

## Problem

Given `n` and `k`, generate all **happy strings** of length `n` using only `a`, `b`, and `c`. A happy string cannot contain the same character consecutively. Return the `k`-th happy string in lexicographical order. If fewer than `k` happy strings exist, return `""`.

## Approach

1. Create the characters `a`, `b`, and `c`.
2. Use `itertools.product()` to generate all possible strings of length `n`.
3. Convert each generated tuple into a string.
4. Check every string to make sure no two consecutive characters are the same.
5. Store valid happy strings in `result`.
6. Return the `(k-1)`th element because Python uses **0-based indexing**.
7. If there are fewer than `k` valid strings, return an empty string.

```python
chars = ['a', 'b', 'c']
combinations = itertools.product(chars, repeat=n)
items = [''.join(ele) for ele in combinations]
```

Then validate each string:

```python
for i in range(len(item)-1):
    if item[i] == item[i+1]:
        isRepeat = True
        break
```

Finally, return the required string:

```python
if len(result) < k:
    return ""
else:
    return result[k-1]
```

## Python Concepts Used

* **`itertools.product()`** – Generates all possible character combinations.
* **Lists** – Store generated strings and valid happy strings.
* **String joining** – Convert tuples into strings using `''.join()`.
* **String indexing** – Compare consecutive characters.
* **Boolean flags** – Use `isRepeat` to track repeated characters.
* **0-based indexing** – Access the `k`-th string using `result[k-1]`.

## Time Complexity

**O(3ⁿ × n)** — There are `3ⁿ` possible strings, and checking each string takes O(n).

## Space Complexity

**O(3ⁿ × n)** — Stores all generated strings and valid happy strings.

## Key Learning

When generating strings with restrictions, we can first generate possible combinations and then **validate each combination** based on the required condition.
