# LeetCode 1700 - Number of Students Unable to Eat Lunch

## Problem

Given two arrays, `students` and `sandwiches`, determine how many students are unable to eat lunch. Students prefer either circular or square sandwiches, represented by `0` and `1`. Students take sandwiches in order, and the process stops when the student at the front cannot eat the sandwich on top of the stack.

## Approach

1. Use `Counter(students)` to count how many students prefer each sandwich type.
2. Iterate through the `sandwiches` array in order.
3. If at least one student prefers the current sandwich, decrease that preference count by one.
4. If no student prefers the current sandwich, stop processing using `break`.
5. Return the sum of the remaining student counts.

```
student_collection = Counter(students)for sandwich in sandwiches:    if student_collection[sandwich] > 0:        student_collection[sandwich] -= 1    else:        breakreturn sum(student_collection.values())
```

## Python Concepts Used

- `Counter` from the `collections` module
- Dictionaries and frequency counting
- `for` loops
- Conditional statements
- `break`
- Dictionary value updates
- `sum()` and `.values()`

## Time Complexity

O(n), where `n` is the number of students, assuming each `Counter` operation takes O(1) on average.

## Space Complexity

O(1) auxiliary space because there are only two possible sandwich preference types, `0` and `1`, so the counter stores at most two keys.

## Key Learning

`Counter` makes frequency-based problems easier by tracking how many students prefer each type. Instead of simulating the entire student queue, the solution uses preference counts to determine whether each sandwich can be consumed.
