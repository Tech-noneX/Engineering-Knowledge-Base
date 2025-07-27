---
id: map
title: 'map()'
section: 'Built-in Functions'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Applies a function to every item in one or more iterables, returning an iterator'
tags: ['built-in', 'function', 'map', 'apply', 'iterator', 'iterable', 'transformation']
see_also: ['filter()', 'zip()', 'list()', 'comprehension', 'map() real-world **R.W.E**']
works_with: ['list', 'tuple', 'str', 'set', 'range', 'iterable']
---

# map()

- **Used with:** Iterables (lists, tuples, strings, sets, etc.)
- **Construct:** function (returns an iterator)
- **Library:** Built-in
- **Iterable:** Yes (returns an iterator)
- **Time Complexity:** O(n), where n = length of the shortest iterable

## Description

The `map()` function applies a given function to each item of one or more iterables (like lists or tuples) and returns an iterator with the results.  
Commonly used for transforming data, converting types, or applying calculations to all items in a sequence.  
Stops at the shortest input if multiple iterables are provided.

## Usable With

Use `map()` with any function (can be built-in, lambda, or custom) and any iterable(s): lists, tuples, strings, sets, etc.

## Syntax

```python
map(function, iterable, ...)
```

- **explanation:**  
  - `function` (required): Function to apply to each item (must take as many arguments as there are iterables).
  - `iterable` (required): One or more iterables (lists, tuples, etc.).
  - Returns an iterator with results.

## Arguments

- **Required:** 2 (function, iterable)
- **Optional:** Unlimited (can add more iterables)
- **Maximum:** Unlimited

- Required:

```python
nums = [1, 2, 3]
doubled = map(lambda x: x * 2, nums)  # iterator of 2, 4, 6
```

- Optional:

```python
# Multiple iterables: function must take as many arguments
a = [1, 2, 3]
b = [10, 20, 30]
summed = map(lambda x, y: x + y, a, b)  # 11, 22, 33
```

- Maximum

```python
# map() works with as many iterables as you want, function must accept that many args
result = map(lambda x, y, z: x + y + z, [1, 2], [3, 4], [5, 6])
# result yields 9, 12
```

## Examples

- **Apply a function to each item in a list**

```python
nums = [1, 2, 3]
squares = list(map(lambda x: x ** 2, nums))
# squares is [1, 4, 9]
```

- **Convert all strings to integers**

```python
data = ['1', '2', '3']
ints = list(map(int, data))
# ints is [1, 2, 3]
```

- **Map with multiple iterables**

```python
a = [1, 2, 3]
b = [10, 20, 30]
result = list(map(lambda x, y: x + y, a, b))
# result is [11, 22, 33]
```

**Note:**  
`map()` returns an **iterator**—wrap in `list()` or loop to access results.  
Stops when the shortest iterable is exhausted.

## Tips & Common mistakes

- Always use `list(map(...))` or a loop if you want the results as a list (especially in Python 3).
- For simple transformations, list comprehensions are often clearer and more Pythonic.
- The function must accept as many arguments as there are iterables.
- Stops at the shortest input; extra items in longer iterables are ignored.

```python
words = ['a', 'b', 'c']
upper = list(map(str.upper, words))
# upper is ['A', 'B', 'C']
```

## See Also

- [`filter()`](filter)
- [`zip()`](zip)
- [`list()`](list)
- [`comprehension`](comprehension)
- [`map() real-world` **R.W.E**](map_rwe)
