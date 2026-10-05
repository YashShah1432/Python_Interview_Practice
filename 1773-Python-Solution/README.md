# LeetCode 1773 - Count Items Matching a Rule

## Problem

Given a list of items where each item contains a `type`, `color`, and `name`, count how many items match the given `ruleKey` and `ruleValue`.

## Approach

1. Initialize `count` to `0`.
2. Iterate through every item.
3. Check which `ruleKey` is provided:
   - `"type"` → compare with `items[i][0]`
   - `"color"` → compare with `items[i][1]`
   - `"name"` → compare with `items[i][2]`
4. If the corresponding value matches `ruleValue`, increment `count`.
5. Return the final count.

```python
count = 0

for i in range(len(items)):
    if (ruleKey == "type" and ruleValue == items[i][0]) or \
       (ruleKey == "color" and ruleValue == items[i][1]) or \
       (ruleKey == "name" and ruleValue == items[i][2]):
        count += 1

return count
```

## Python Concepts Used

- Lists and nested lists
- Indexing
- `for` loop
- `range()` and `len()`
- Conditional statements
- Logical `and` and `or` operators
- Counter variable

## Time Complexity

**O(n)**, where `n` is the number of items.

## Space Complexity

**O(1)** because only a counter variable is used apart from the input.

## Key Learning

Nested lists can be accessed using indexes to compare specific attributes. Combining `and` and `or` conditions allows different matching rules to be handled within a single condition.
