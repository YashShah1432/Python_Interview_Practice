# LeetCode 232 - Implement Queue using Stacks

## Problem

Implement a queue using two stacks. The queue should support `push`, `pop`, `peek`, and `empty` operations while following the FIFO (First In, First Out) principle.

## Approach

1. Initialize two stacks, `stack1` and `stack2`.
2. During `push`:
   - Move all elements from `stack1` to `stack2`.
   - Push the new element into `stack1`.
   - Move all elements back from `stack2` to `stack1`.
3. During `pop`, remove and return the last element of `stack1`.
4. During `peek`, return the last element of `stack1` without removing it.
5. During `empty`, check whether `stack1` is empty.

```
def push(self, x: int) -> None:    while len(self.stack1) > 0:        self.stack2.append(self.stack1.pop())    self.stack1.append(x)    while len(self.stack2) > 0:        self.stack1.append(self.stack2.pop())def pop(self) -> int:    return self.stack1.pop()def peek(self) -> int:    return self.stack1[-1]def empty(self) -> bool:    return len(self.stack1) == 0
```

## Python Concepts Used

- Classes and objects
- Constructor using `__init__()`
- Lists as stacks
- `append()` and `pop()`
- `while` loops
- `len()`
- Negative indexing
- Boolean return values

## Time Complexity

- `push()` — O(n): Moves all existing elements between the two stacks.
- `pop()` — O(1): Removes the last element from `stack1`.
- `peek()` — O(1): Accesses the last element of `stack1`.
- `empty()` — O(1): Checks whether `stack1` is empty.

## Space Complexity

O(n) for storing the queue elements across the two stacks.

## Key Learning

A queue follows FIFO, while a stack follows LIFO. By transferring elements between two stacks during `push()`, the oldest element stays at the top of `stack1`, allowing `pop()` and `peek()` to work in constant time.
