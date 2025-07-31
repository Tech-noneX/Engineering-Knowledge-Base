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
file_path: docs/datatypes/list_datatype.md
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

- Lists are mutable (items can be added, changed, or removed)
- Items are indexed starting from 0
- Supports slicing and negative indices

## Common Methods & Functions

- `append()`, `extend()`, `insert()`, `pop()`, `remove()`, `reverse()`, `sort()`
- See full list in the “See Also” section

## Examples

```python
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # ['apple', 'banana', 'cherry']
```

## Tips & Common Mistakes

- Don’t forget that lists are mutable: changes to one list can affect another if you copy by reference
- Use `.copy()` or `list()` to clone a list if you want a new object

## See Also

- [`tuple`](tuple)
- [`set`](set)
- [`dict`](dict)
- [`append()`](append)
- [`pop()`](pop)
- [`extend()`](extend)
- [`slicing`](slicing)
- [`comprehension`](comprehension)
