---
id: int
title: int
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Whole number type; used for integers in Python (positive, negative, or zero).
tags: ['data type', 'int', 'integer', 'number', 'numeric', 'math']
see_also: ['float', 'complex', 'str', 'list', 'abs', 'round']
works_with: ['float', 'str', 'list', 'set', 'dict', 'for', 'in']
file_path: docs/datatypes/int_datatype.md
---

# int

## Description

An **int** is a whole number—positive, negative, or zero—without any decimal places.  

- Used for counting, indexing, math, and any situation where only whole numbers are allowed.
- Supports all basic math operations, bitwise operations, and comparisons.
- Has unlimited precision (can be arbitrarily large).

Commonly used for loops, array indices, math, and data storage.

## Usable With

- Works with all numeric types (`float`, `complex`), as well as strings (with `int()` conversion).
- Usable with built-in functions like `len()`, `sum()`, `min()`, `max()`, `range()`, etc.
- Can be used as dict keys and set elements.

## Creation & Syntax

```python
# Direct assignment:
age = 42

# Negative numbers:
temp = -10

# From other types:
num = int("123")        # From string: 123
whole = int(3.99)       # From float: 3 (truncates decimals)
big = 123_456_789_123_456_78
# Special: large numbers (Python auto-expands as needed)
binary = int("1101", 2) # From binary string: 13
```

 note:
> The second argument in int(string, base) tells Python what number system (base) the string is written in. For example, `int("1101", 2)` reads `"1101"` as binary.

## Key Properties

- **Immutable:** Value cannot be changed after creation (operations return a new int).
- **Unlimited size:** No practical limit for value (besides memory).
- **Hashable:** Can be used as keys in dicts or sets.
- **Supports arithmetic and bitwise operations.**

## Common Methods & Functions

- `int(x)`: Convert a value to int.
- `.bit_length()`: Number of bits to represent the int.
- `.to_bytes()`, `.from_bytes()`: Conversion to/from byte representation.
- Math operations: `+`, `-`, `*`, `//`, `%`, `**`, etc.
- Built-ins: `abs()`, `round()`, `divmod()`, `pow()`

## Examples

```python
# Basic arithmetic
a = 7
b = 3
print(a + b)    # 10
print(a // b)   # 2 (floor division)
print(a % b)    # 1 (modulo)

# Type conversion
n = int("42")       # 42
m = int(8.99)       # 8

# Large integers
big = 10 ** 100     # Valid in Python!

# Using as dict keys
scores = {1: 'A', 2: 'B'}
```

## Tips & Common Mistakes

- **String conversion:**  
  `int("10")` works, but `int("10.5")` will raise an error.  
  Use `float()` first if the string may contain decimals.

- **Truncation:**  
  `int(7.9)` becomes `7` (truncates, does not round).

- **Division:**  
  `/` always returns `float` (even with int inputs); use `//` for integer division.

- **Leading zeros:**  
  Don’t use leading zeros in code (e.g., `012` is invalid in Python 3).

- **Use underscores for readability:**  
  `one_million = 1_000_000` is valid and clearer.

## See Also

- [`float`](float)
- [`complex`](complex)
- [`str`](str)
- [`abs()`](abs)
- [`round()`](round)
