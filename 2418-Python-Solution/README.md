# LeetCode 2418 - Sort the People

## Problem

Given two arrays `names` and `heights`, sort the people in **descending order of height** and return their names in that order.

## Approach

1. Create an empty list `arr`.
2. Combine each person's height and name into a pair `[height, name]`.
3. Sort `arr` in descending order using `sort(reverse=True)`.
4. Traverse the sorted list and extract the names.
5. Return the resulting list.

```python
arr = []
result = []

for i in range(len(names)):
    arr.append([heights[i], names[i]])
    arr.sort(reverse=True)

for j in range(len(arr)):
    result.append(arr[j][1])

return result
```

## Python Concepts Used

* **Lists** – Store height-name pairs and the final names.
* **Nested lists** – Represent each person as `[height, name]`.
* **`append()`** – Add each person to the list.
* **`sort(reverse=True)`** – Sort people by height in descending order.
* **List indexing** – Extract names from the sorted pairs.
* **For loops** – Build and process the lists.

## Time Complexity

**O(n² log n)** — Since the list is sorted inside the first loop, sorting is performed up to `n` times.

## Space Complexity

**O(n)** — The `arr` and `result` lists store `n` elements.

## Key Learning

Combining related values into **nested lists** allows Python's sorting mechanism to order the data based on the first element of each pair.
