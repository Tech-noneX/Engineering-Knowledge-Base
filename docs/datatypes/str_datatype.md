---
id: str
title: str
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Immutable, ordered sequence of characters; used for text in Python.
tags: ['data type', 'str', 'string', 'immutable', 'sequence', 'text']
see_also: ['list', 'bytes', 'tuple', 'int']
works_with: ['list', 'tuple', 'dict', 'set', 'for', 'in']
file_path: docs/datatypes/str.md
---

# str

## Description

A **string** (`str`) is an immutable, ordered sequence of Unicode characters.  

- Used for storing and manipulating text in Python.
- Each character is accessed by its index (starting from 0).
- Strings are immutable: once created, they cannot be changed.

Commonly used for text processing, data input/output, and file operations.

## Usable With

- Used in loops, `for`/`in` statements, and comprehensions.
- Works with many built-in functions: `len()`, `max()`, `min()`, `sorted()`, etc.
- Compatible with `list()`, `tuple()`, and `set()` for type conversions.

## Creation & Syntax

```python
# Using single or double quotes:
name = "Alice"
greeting = 'Hello, world!'

# Multi-line strings:
text = """This is
a multi-line
string."""

# Empty string:
empty = ""

# From other types:
s = str(42)  # '42'
```

## Key Properties

- **Ordered:** Characters maintain order; indexable and sliceable.
- **Immutable:** Cannot change the string after creation.
- **Unicode:** Supports international characters and emojis.
- **Iterable:** Can loop through each character.

## Common Methods & Functions

- `.lower()`, `.upper()`, `.capitalize()`, `.title()`, `.strip()`
- `.split()`, `.join()`, `.replace()`, `.find()`, `.count()`
- `len(str)`, `str()`, slicing, membership: `'a' in s`

## Examples

```python
# Basic usage
message = "Python"
print(message[1])        # 'y'
print(message.upper())   # 'PYTHON'

# Slicing
sub = message[1:4]       # 'yth'

# Joining and splitting
csv = ",".join(['a', 'b', 'c'])     # 'a,b,c'
parts = csv.split(",")              # ['a', 'b', 'c']
```

## Tips & Common Mistakes

- **Immutable:**  
  Cannot modify characters directly. Use methods to create new strings.
  
  ```python
  s = "hi"
  # s[0] = "H"  # ❌ Raises TypeError
  s = "H" + s[1:]  # ✅ 'Hi'
  ```

- **Single vs. double quotes:**  
  Both work the same, but be consistent.

- **Escape characters:**  
  Use `\n` for newlines, `\t` for tabs, and `\\` for a backslash.

- **Multi-line strings:**  
  Use triple quotes (`"""` or `'''`) for multi-line text.

- **Converting other types:**  
  Use `str()` to turn numbers or objects into strings.

## See Also

- [`list`](list)
- [`bytes`](bytes)
- [`tuple`](tuple)
- [`int`](int)
