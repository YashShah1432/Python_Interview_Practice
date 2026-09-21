# LeetCode 2367 - Number of Arithmetic Triplets

## Problem

Given a strictly increasing array `nums` and an integer `diff`, count the number of arithmetic triplets `(nums[i], nums[j], nums[k])` where the difference between consecutive elements is `diff`.

## Approach

1. Convert `nums` into a set for fast membership checking.
2. Iterate through every number in `nums`.
3. Check whether both `num - diff` and `num + diff` exist in the set.
4. If both exist, a valid arithmetic triplet is formed.
5. Increment `count` and return the final result.

```python
count = 0
num_set = set(nums)

for num in nums:
    if num - diff in num_set and num + diff in num_set:
        count += 1

return count
```

## Python Concepts Used

* **Sets** – Store numbers for fast membership checking.
* **Set membership** – Use `in` to check whether required values exist.
* **For loop** – Iterate through each number.
* **Conditional statements** – Verify both required values.
* **Counter variable** – Track the number of valid triplets.

## Time Complexity

**O(n)** — Creating the set and iterating through `nums` both take O(n) average time.

## Space Complexity

**O(n)** — The set stores all elements of `nums`.

## Key Learning

Using a **set for membership checking** can reduce repeated searching from linear time to average **O(1)**, making it efficient to identify arithmetic triplets.
