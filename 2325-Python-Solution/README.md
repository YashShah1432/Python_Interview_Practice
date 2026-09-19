# LeetCode 2325 - Decode the Message

## Problem

Given a `key` and an encoded `message`, decode the message using the substitution mapping created from the **first occurrence of each letter** in the key. Spaces remain unchanged.

## Approach

1. Traverse the `key` and build a string containing each unique character, ignoring spaces.
2. The position of each character in this string represents its corresponding alphabet position.
3. Traverse the `message` character by character.
4. Keep spaces unchanged.
5. For other characters, find their position in `new_str` and convert that position into the corresponding lowercase letter using `chr()` and `ord()`.
6. Return the decoded message.

```python id="6s5xsl"
new_str = ''

for char in key:
    if char not in new_str and char != " ":
        new_str += char
```

The message is then decoded using the character's position in the mapping:

```python id="p2b7wq"
if message[i] == " ":
    ans += " "
else:
    ans += chr(ord('a') + new_str.index(message[i]))
```

## Python Concepts Used

* **Strings** – Build the substitution mapping and decoded message.
* **`in` operator** – Check whether a character is already present.
* **`index()`** – Find the position of a character in the mapping.
* **`ord()`** – Get the ASCII value of a character.
* **`chr()`** – Convert an ASCII value back to a character.
* **String concatenation** – Build the mapping and final answer.

## Time Complexity

**O(n × m)** — Where `n` is the length of `key` and `m` is the length of `message`. String membership and `index()` operations can take linear time.

## Space Complexity

**O(n + m)** — `new_str` stores the unique key characters and `ans` stores the decoded message.

## Key Learning

A substitution cipher can be implemented by creating a **character-to-position mapping** from the key and then using each character's position to determine its decoded alphabet character.
