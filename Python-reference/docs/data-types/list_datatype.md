---
id: list
title: list
section: 'Data Types'
module: 'built-in'
difficulty: beginner
subscription: premium
reference: "Mutable ordered collection of items, usually of the same or similar types."
tags: ['data type', 'list', 'sequence','mutable', 'iterable', 'built-in']
see_also: ['tuple', 'set', 'dict', 'append()', 'pop()', 'extend()', 'slicing', 'comprehension']
works_with: []
file_path: Python-reference/docs/data-types/list_datatype.md
---

# list

## Description

A `list` in Python is a flexible, mutable, and ordered collection of items. Lists are perfect for storing sequences of data that may change during the program, like names, results, or settings. Lists can hold any data type including numbers, strings, or even other lists—making them one of Python’s most commonly used and versatile data types.

### Lists allow you to

- Add or remove items at any position
- Store elements in a specific order (order is preserved)
- Iterate through items easily with loops
- Slice or reverse the collection with simple syntax
- Unlike `tuples`, lists can be changed after creation. If you need to store a collection of items where the order and ability to update matter, use a list.

## Usable With

- Any iterable, including strings, tuples, ranges, other lists, etc.

## Creation & Syntax

```python
# Creating a list
numbers = [1, 2, 3]
words = ["apple", "banana", "cherry"]

# Using list()
chars = list("hello")
empty = list()
```

## Key Properties

- **Ordered:** Items keep their insertion order.
- **Mutable:** Items can be added, changed, or removed.
- **Indexed:** The first item is index `0`; negative indexes count from the end.
- **Sliceable:** A slice such as `items[1:4]` returns a new list.
- **Duplicates allowed:** The same value may appear more than once.

## Common Methods & Functions

- `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `reverse()`, `sort()`
- See full list in the “See Also” section

## Examples

```python
# Indexing and slicing
measurements = [12.4, 12.7, 13.1, 12.9]
print(measurements[0])    # 12.4
print(measurements[1:3])  # [12.7, 13.1]

# Add and remove items
fruits = ["apple", "banana"]
fruits.append("cherry")
removed = fruits.pop(0)
print(removed)  # 'apple'
print(fruits)   # ['banana', 'cherry']

# Build a new list with a comprehension
squares = [number ** 2 for number in range(1, 5)]
print(squares)  # [1, 4, 9, 16]
```

## Tips & Common Mistakes

- Don’t forget that lists are mutable: assigning one list to another variable does not copy it.
- Use `.copy()`, slicing (`items[:]`), or `list(items)` when you need a shallow copy.
- A shallow copy still shares nested mutable objects with the original list.

```python
original = [[1, 2], [3, 4]]
alias = original
copy = original.copy()

alias.append([5, 6])       # Also changes original
copy[0].append(99)         # Nested list is shared with original
```

## See Also

- [`tuple`](tuple)
- [`set`](set)
- [`dict`](dict)
- [`append()`](append)
- [`pop()`](pop)
- [`extend()`](extend)
- [`slicing`](slicing)
- [`comprehension`](comprehension)
