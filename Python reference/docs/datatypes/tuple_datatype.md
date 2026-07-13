---
id: tuple
title: tuple
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Immutable, ordered collection of items, often used for fixed data.
tags: ['data type', 'tuple', 'immutable', 'sequence']
see_also: ['list', 'set', 'dict', 'namedtuple']
works_with: ['list', 'set', 'dict', 'for', 'in']
file_path: docs/datatypes/tuple_datatype.md
---

# tuple

## Description

A **tuple** is an immutable, ordered collection of items.  

- Items are stored in a specific sequence and can be accessed by index.
- Once created, a tuple **cannot be changed** (no adding, removing, or replacing items).
- Useful for representing **fixed collections** of values, function return values, or keys in dictionaries.

Commonly used to group related data, return multiple values from functions, or use as dictionary keys.

## Usable With

- Can be used in **loops**, `for` and `in` statements, and unpacking assignments.
- Works with `len()`, `sum()`, `min()`, `max()`, `sorted()`, and many built-in functions.
- Compatible with `list()`, `set()`, and `dict()` for conversions.

## Creation & Syntax

```python
# Creating a tuple with parentheses:
numbers = (1, 2, 3)

# Or without parentheses (comma is enough, but not recommended for clarity):
colors = 'red', 'green', 'blue'

# Empty tuple:
empty = ()

# Single-item tuple (MUST include a comma):
single = (42,)
```

## Key Properties

- **Ordered:** Items keep their order; indexable.
- **Immutable:** Cannot be changed after creation.
- **Can contain any data type:** Including other tuples, lists, or mixed types.
- **Hashable:** Can be used as dictionary keys (if all elements are hashable).

## Common Methods & Functions

- `.count(x)` – Count how many times `x` appears in the tuple.
- `.index(x)` – Return the index of the first occurrence of `x`.
- `len(tuple)` – Number of items.
- Support for unpacking (`a, b = t`), slicing (`t[1:3]`), and membership testing (`x in tuple`).

## Examples

```python
# Creating and using tuples
person = ('Alice', 30, 'Engineer')
print(person[0])   # 'Alice'

# Tuple unpacking
x, y = (5, 10)
print(x + y)       # 15

# Nested tuples
matrix = ((1, 2), (3, 4))
print(matrix[1][0])  # 3
```

## Tips & Common Mistakes

- **Don’t forget the comma for single-item tuples:**  
  `t = (5,)` is a tuple; `t = (5)` is just the number 5.

- **Immutable:**  
  You can’t change, add, or remove items after creation.  

  ```python
  t = (1, 2, 3)
  # t[0] = 10  # ❌ This will raise an error
  ```

- **Use lists if you need to modify:**  
  Tuples are for *fixed* collections; use lists for changing data.

- **Can be used as dict keys:**  
  Only if all elements inside are hashable.

- **Supports unpacking:**  

  ```python
  name, age = ('Tom', 40)
  ```

## See Also

- [`list`](list)
- [`set`](set)
- [`dict`](dict)
- [`namedtuple`](namedtuple)
