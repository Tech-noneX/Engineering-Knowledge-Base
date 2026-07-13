---
id: add
title: 'add()'
section: 'Set Methods'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Adds a single element to a set if not already present'
tags: ['set', 'method', 'add', 'unique', 'collection', 'mutable']
see_also: ['remove()', 'discard()', 'update()', 'add() set union **R.W.E**']
works_with: ['set']
---

# add()

- **Used with:** set
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (adds a single item per call)
- **Time Complexity:** O(1) average (amortized), but can be worse in rare cases

## Description

The `add()` method adds a single element to a set.  
If the element is already present, the set remains unchanged (no error, no duplicate).  
Does nothing if the value exists—sets only contain unique items.

## Usable With

Use with mutable sets only (`set`, not `frozenset`).  
Accepts any hashable object (numbers, strings, tuples, etc.).

## Syntax

```python
set.add(element)
```

- **explanation:**  
  - `element`: The item to add to the set (must be hashable).

## Arguments

- **Required:** 1 (`element`)

- **Optional:** 0

- **Maximum:** 1

- Required:

```python
numbers = {1, 2, 3}
numbers.add(4)
# numbers is now {1, 2, 3, 4}
```

- Optional:

```python
# No optional arguments; only the element is required
```

- Maximum

```python
# Only one argument allowed (the element)
```

## Examples

- **Add a string to a set**

```python
letters = {'a', 'b'}
letters.add('c')
# letters is now {'a', 'b', 'c'}
```

- **Try to add an existing item (no error, no duplicate)**

```python
colors = {'red', 'green'}
colors.add('red')
# colors is still {'red', 'green'}
```

- **Add a tuple (hashable) but not a list (unhashable)**

```python
pairs = set()
pairs.add((1, 2))  # OK
# pairs.add([3, 4])  # Error: unhashable type: 'list'
```

**Note:**  
`add()` returns `None` (it does not return the set).

## Tips & Common mistakes

- Only works with **sets** (not lists, dicts, or tuples).
- Raises `TypeError` if the element is unhashable (e.g., list, dict, set).
- For adding multiple items, use `set.update(iterable)` instead.
- No error if the item already exists—set stays unchanged.

```python
nums = {1, 2}
nums.add(2)
# nums is still {1, 2}
```

## See Also

- `remove()`
- `discard()`
- `update()`
- `add() set union` **R.W.E**
