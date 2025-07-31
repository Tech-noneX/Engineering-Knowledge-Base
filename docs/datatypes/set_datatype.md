---
id: set
title: set
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Unordered, mutable collection of unique, hashable items.
tags: ['data type', 'set', 'unique', 'collection', 'mutable', 'hash']
see_also: ['frozenset', 'list', 'dict', 'tuple', 'union', 'intersection']
works_with: ['list', 'tuple', 'str', 'dict', 'for', 'in']
file_path: docs/datatypes/set_datatype.md
---

# set

## Description

A **set** is an unordered, mutable collection of unique, hashable items.

- Used to store distinct elements and remove duplicates automatically.
- Great for set operations: union, intersection, difference, symmetric difference.
- Items must be hashable (e.g., numbers, strings, tuples).

Commonly used for fast membership testing, removing duplicates, and mathematical set logic.

## Usable With

- Can be created from lists, tuples, strings, and other iterables.
- Works with loops (`for`/`in`), comprehensions, and set methods.
- Many built-in functions work: `len()`, `sum()`, `min()`, `max()`, etc.

## Creation & Syntax

```python
# Curly braces for non-empty sets:
colors = {'red', 'green', 'blue'}

# Using set() constructor (for empty set or converting iterables):
unique_nums = set([1, 2, 2, 3])  # {1, 2, 3}
letters = set("hello")           # {'h', 'e', 'l', 'o'}

# Empty set (must use set(), not {}):
empty = set()
```

## Key Properties

- **Unordered:** No index; elements have no order.
- **Mutable:** Can add or remove elements.
- **Unique items only:** Duplicates are removed automatically.
- **Hashable items only:** Can’t contain lists or dicts.

## Common Methods & Functions

- `.add(x)`, `.remove(x)`, `.discard(x)`, `.pop()`, `.clear()`
- `.union()`, `.intersection()`, `.difference()`, `.symmetric_difference()`
- `.issubset()`, `.issuperset()`, `.copy()`
- Membership: `x in set`
- Built-ins: `len(set)`, `set()`

## Examples

```python
# Removing duplicates from a list
nums = [1, 2, 2, 3, 4, 4]
unique = set(nums)      # {1, 2, 3, 4}

# Set operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)            # {1, 2, 3, 4, 5} (union)
print(a & b)            # {3}             (intersection)
# Set difference (elements in a but NOT in b)
a = {1, 2, 3}
b = {3, 4, 5}
print(a - b)   # {1, 2}

# Set symmetric difference (elements in a or b, but NOT both)
print(a ^ b)   # {1, 2, 4, 5}


# Adding and removing elements
colors = {'red', 'blue'}
colors.add('green')
colors.remove('red')
```

## Tips & Common Mistakes

- **Empty set:**  
  Use `set()`, not `{}` (which creates an empty dict).

- **No indexing or order:**  
  Cannot access items by index or slice. Convert to list if needed.

- **Hashable only:**  
  Items must be hashable (immutable). Lists and dicts cannot be in a set.

- **Set operations:**  
  Use operators (`|`, `&`, `-`, `^`) or methods (`union()`, etc.).

- **Duplicates automatically removed:**  
  When converting an iterable to a set, only unique items are kept.

## See Also

- [`frozenset`](frozenset)
- [`list`](list)
- [`dict`](dict)
- [`tuple`](tuple)
- [`union()`](union)
- [`intersection()`](intersection)
