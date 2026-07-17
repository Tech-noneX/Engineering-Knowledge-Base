---
id: dict
title: dict
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Mutable, insertion-ordered key-value mapping for structured data.
tags: ['data type', 'dict', 'mapping', 'mutable', 'key-value', 'hash']
see_also: ['list', 'set', 'tuple', 'defaultdict', 'Counter', 'items']
works_with: ['list', 'tuple', 'str', 'set', 'for', 'in']
file_path: Python-reference/docs/data-types/dict_datatype.md
---

# dict

## Description

A **dictionary** (`dict`) is a mutable mapping of unique keys to values. Modern
Python dictionaries preserve the order in which keys were inserted.
- Each value is associated with a unique key (keys must be hashable and unique).
- Used for storing structured data, fast lookups, and flexible mappings.
- Allows dynamic adding, changing, and removing of keys and values.

Commonly used for databases, config data, mapping names to values, and more.

## Usable With

- Used in loops, `for`/`in` statements, and comprehensions.
- Keys must be hashable: common examples include strings, numbers, and tuples whose items are also hashable.
- Works with many built-in functions (`len()`, `list()`, `dict()`, `keys()`, `values()`, etc.).
- Easily convertible to/from lists of tuples.

## Creation & Syntax

```python
# Using curly braces:
person = {'name': 'Alice', 'age': 30}

# Using the dict constructor:
info = dict(city='London', country='UK')

# Empty dict:
empty = {}

# From an iterable of key-value pairs:
grades = dict([('math', 90), ('art', 80)])

# From another mapping plus keyword arguments:
settings = dict({'voltage': 230}, phase='single')
```

## Key Properties

- **Insertion ordered:** Order has been guaranteed by the language since Python 3.7.
- **Mutable:** Can add, change, or remove keys and values.
- **Keys must be unique and hashable:** (strings, numbers, tuples, etc.)
- **Fast lookup by key.**

## Common Methods & Functions

- `.get(key)`, `.setdefault(key)`, `.pop(key)`, `.update(other)`
- `.keys()`, `.values()`, `.items()`
- `len(dict)`, `dict()`, `in` (for checking if key exists)

## Examples

```python
# Creating and accessing dictionaries
user = {'username': 'bob', 'score': 120}
print(user['score'])   # 120

# Adding and updating keys
user['level'] = 5      # add new key
user['score'] += 30    # update value

# Looping through items
for k, v in user.items():
    print(k, v)
```

## Tips & Common Mistakes

- **KeyError:**  
  Accessing a missing key raises a `KeyError`. Use `.get()` for a safe default.
  ```python
  user.get('rank', 0)  # returns 0 if 'rank' is missing
  ```

- **Mutable:**  
  Changes affect all references to the same dict.

- **Order preservation:**  
  Updating an existing key does not move it. Deleting and reinserting a key places it at the end.

- **Immutable keys only:**  
  Lists and other dicts can’t be keys.

- **Copying:**  
  Use `copy()` for a shallow copy; changes to nested objects still affect the original.

## See Also

- [`list`](list)
- [`set`](set)
- [`tuple`](tuple)
- [`defaultdict`](defaultdict)
- [`Counter`](Counter)
- [`items()`](items)
