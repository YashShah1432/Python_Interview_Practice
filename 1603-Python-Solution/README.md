# LeetCode 1603 - Design Parking System

## Problem

Design a parking system for three types of parking spaces: big, medium, and small. Implement the `ParkingSystem` class so that `addCar(carType)` returns `True` if a suitable parking space is available and parks the car, or `False` if no space is available.

## Approach

1. Initialize a list `count` containing the available big, medium, and small parking spaces.
2. Use `carType - 1` as the index to access the corresponding parking space:
   - `1` → Big
   - `2` → Medium
   - `3` → Small
3. Check whether the selected parking space has available capacity.
4. If capacity is available, decrement the count and return `True`.
5. Otherwise, return `False`.

```
class ParkingSystem:    def __init__(self, big: int, medium: int, small: int):        self.count = [big, medium, small]    def addCar(self, carType: int) -> bool:        if self.count[carType - 1] > 0:            self.count[carType - 1] -= 1            return True        return False
```

## Python Concepts Used

- Classes and objects
- `__init__()` constructor
- Instance variables using `self`
- Lists and indexing
- Conditional statements
- Decrement operator (`-=`)
- Boolean return values

## Time Complexity

O(1) per `addCar()` operation because it accesses and updates a list element directly.

## Space Complexity

O(1) because the list always contains exactly three elements.

## Key Learning

A list can efficiently track the remaining capacity of different parking space types. Using `carType - 1` maps the car type directly to its corresponding list index, allowing constant-time updates.
