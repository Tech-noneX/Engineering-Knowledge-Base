---
id: range
title: "range()"
section: "Built-in Functions"
module: "build-in"
difficulty: beginner
subscription: free
reference: "Generates a sequence of numbers for looping or indexing"
tags: ["built-in", "function", "range", "sequence", "iteration", "for loop", "integer"]
see_also: ["list()", "for", "enumerate()", "reversed()", "range() pagination"]
works_with: ["int", "for loop", "iteration"]
---

# range()

- **Used with:** Integers (int), loops, iteration
- **Construct:** function (returns an immutable sequence type)
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(1) for creating, O(n) for iteration (n = size of range)

## Description

The `range()` function generates an immutable sequence of numbers, commonly used for looping a specific number of times. It does **not** create a list in memory (efficient for large ranges), but returns a special `range` object that can be iterated over.

## Usable With

Use `range()` for any situation where you need a sequence of integers, such as in for-loops, indexing, slicing, or generating number lists.

## Syntax

```python
range(stop)
range(start, stop[, step])
```

- **explanation:**
  - `range(stop)` – Generates numbers from 0 up to (but not including) stop.
  - `range(start, stop)` – Numbers from start up to (but not including) stop.
  - `range(start, stop, step)` – Numbers from start up to stop, stepping by step (can be negative).

## Arguments

- **Required:**
  - 1 (`stop`)  
  - or 2 (`start`, `stop`)
- **Optional:**
  - 1 (`step`, int, default is 1)
- **Maximum:** 3

```python
# Just stop
r1 = range(5)  # 0, 1, 2, 3, 4

# Start and stop
r2 = range(2, 6)  # 2, 3, 4, 5

# With step
r3 = range(1, 10, 2)  # 1, 3, 5, 7, 9
```

## Examples

- **Basic loop with range**

```python
for i in range(3):
    print(i)
# Output: 0 1 2
```

- **Custom start and stop**

```python
for x in range(5, 8):
    print(x)
# Output: 5 6 7
```

- **Range with step (skip numbers)**

```python
for n in range(0, 10, 3):
    print(n)
# Output: 0 3 6 9
```

- **Convert range to list**

```python
nums = list(range(4))
print(nums)  # Output: [0, 1, 2, 3]
```

**Note:** The stop value is **not included**. Step can be negative to count backwards.

## Tips & Common mistakes

- `range()` does **not** include the stop value.
- If step is negative, start must be greater than stop for results (e.g., `range(5, 0, -1)`).
- `range()` returns a range object (not a list). Convert to list with `list(range(...))` if you need indexing or slicing.
- All arguments must be integers (no floats allowed).
- Range object supports indexing and `in`, but is immutable.

```python
# Counting down
print(list(range(5, 0, -1)))  # [5, 4, 3, 2, 1]
```

## See Also

- `list()`
- `for`
- `enumerate()`
- `reversed()`
- `range() pagination` **R.W.E**
