---
id: union
title: union()
section: Set Methods
module: set
subscription: premium
difficulty: beginner
reference: Returns a new set with all unique elements from two or more sets.
tags: ['method', 'set', 'union', 'combine', 'unique']
see_also: ['update', 'intersection', 'difference', 'symmetric_difference', 'copy']
works_with: ['set']
file_path: docs/sets/methods/union_method.md
---

# union()

- **Used with:** sets (`set`)
- **Construct:** `set.union(*others)` or `set1 | set2`
- **Library:** Built-in
- **Iterable:** Yes (combines all elements from sets and set-like iterables)
- **Time Complexity:** O(len(s) + len(others)) (depends on input sizes)

## Description

The `union()` method returns a **new set** containing all unique elements from the set and one or more other sets or iterables.

- It does **not** modify the original set.
- Equivalent to using the `|` operator (pipe).
- **Duplicates are automatically removed**.

Commonly used to combine elements from multiple collections.

## Usable With

- Works with `set` objects.
- Also accepts any iterable (like lists, tuples), but their elements must be hashable.

## Syntax

```python
set1.union(set2, set3, ...)
# or using the operator:
set1 | set2 | set3
```

- `set2`, `set3`, ...: Other sets or iterables to include.

## Arguments

- **Required:**  
  - At least one other set or iterable is optional. Can be called with no arguments, which just returns a copy of the original set.

```python
a = {1, 2, 3}
b = {3, 4}
a.union(b)   # {1, 2, 3, 4}
```

- **Optional:**  
  - You can pass multiple sets/iterables at once.

```python
a = {1, 2}
b = {2, 3}
c = {3, 4}
a.union(b, c)   # {1, 2, 3, 4}
```

- **Maximum:**  
  - Accepts any number of arguments.

```python
numbers = {1, 2}
numbers.union([2, 3, 4], (4, 5))   # {1, 2, 3, 4, 5}
```

## Examples

- **Combine two sets:**

```python
odds = {1, 3, 5}
evens = {2, 4, 6}
all_numbers = odds.union(evens)
# {1, 2, 3, 4, 5, 6}
```

- **Union with lists/tuples:**

```python
s = {1, 2}
result = s.union([2, 3], (4, 5))
# {1, 2, 3, 4, 5}
```

- **Using | operator:**

```python
a = {1, 2}
b = {3, 4}
combined = a | b
# {1, 2, 3, 4}
```

**Note:**  
Original sets are not changed—union always returns a new set.

## Tips & Common mistakes

- **Original set not modified:**  
  Always returns a new set—assign or use the result.
  
  ```python
  s = {1, 2}
  s.union({3, 4})
  print(s)  # {1, 2}
  ```

- **Can combine any number of sets or iterables:**  
  `a.union(b, c, d, ...)` is valid.

- **Only hashable elements allowed:**  
  Passing an iterable with unhashable elements (like lists) will raise a `TypeError`.

- **Empty argument just returns a copy:**  
  `a.union()` returns a shallow copy of `a`.

## See Also

- [`update()`](update)
- [`intersection()`](intersection)
- [`difference()`](difference)
- [`symmetric_difference()`](symmetric_difference)
- [`copy()`](copy)
