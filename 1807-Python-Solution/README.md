# LeetCode 1807 - Evaluate the Bracket Pairs of a String

## Problem

Given a string `s` containing bracketed keys and a list of key-value pairs `knowledge`, replace each key inside brackets with its corresponding value. If a key is not present in `knowledge`, replace it with `"?"`.

## Approach

1. Convert `knowledge` into a dictionary for efficient key-value lookup.
2. Traverse the string character by character.
3. When `(` is encountered, start collecting the key.
4. While inside the brackets, add each character to `current_key`.
5. When `)` is encountered, convert the collected characters into a string and look up its value in the dictionary.
6. Use `"?"` when the key does not exist.
7. Append normal characters directly to the result.
8. Join the result list and return the final string.

```python
k_dict = {key: value for key, value in knowledge}

res = []
is_inside_brackets = False
current_key = []

for char in s:
    if char == '(':
        is_inside_brackets = True
    elif char == ')':
        is_inside_brackets = False
        key_str = "".join(current_key)

        res.append(k_dict.get(key_str, "?"))

        current_key = []
    elif is_inside_brackets:
        current_key.append(char)
    else:
        res.append(char)

return "".join(res)
```

## Python Concepts Used

* **Dictionary comprehension** – Convert `knowledge` into a dictionary.
* **Dictionaries** – Perform key-value lookups using `get()`.
* **Lists** – Store result characters and bracket contents.
* **String `join()`** – Convert lists of characters into strings.
* **Boolean flags** – Track whether the current character is inside brackets.
* **Conditional statements** – Handle opening brackets, closing brackets, and normal characters.

## Time Complexity

**O(n + k)** — Where `n` is the length of `s` and `k` is the total number of characters in `knowledge`.

## Space Complexity

**O(n + k)** — The dictionary and result storage require additional space.

## Key Learning

Using a **dictionary for key-value mapping** combined with a state flag makes it straightforward to parse bracketed expressions and replace them with their corresponding values.
