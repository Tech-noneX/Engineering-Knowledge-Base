---
id: float
title: float
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Binary floating-point number type used for approximate real-number calculations.
tags: ['data type', 'float', 'decimal', 'number', 'numeric', 'math']
see_also: ['int', 'complex', 'str', 'round', 'math']
works_with: ['int', 'str', 'list', 'set', 'dict', 'for', 'in']
file_path: Python-reference/docs/data-types/float_datatype.md
---

# float

## Description

A **float** is Python's binary floating-point number type, used for approximate
real-number calculations and values with fractional parts.
- Used for measurements, scientific calculations, and any data that requires decimals.
- Supports positive/negative numbers, zero, special values (`inf`, `-inf`, `nan`).

Commonly used for math, data analysis, physics, measurements, and engineering.
Use `decimal.Decimal` instead when exact base-10 arithmetic is required, such as
money calculations.

## Usable With

- Works with all numeric types (`int`, `complex`), and with strings (via `float()` conversion).
- Usable with built-in functions: `abs()`, `round()`, `sum()`, `min()`, `max()`, etc.
- Can be used as keys in dicts and sets.

## Creation & Syntax

```python
# Direct assignment:
price = 9.99

# Scientific notation:
small = 1.5e-10     # 1.5 × 10⁻¹⁰

# From other types:
value = float("3.14")   # From string: 3.14
whole = float(10)       # From int: 10.0

# Special values:
pos_inf = float('inf')      # Infinity
neg_inf = float('-inf')     # Negative infinity
not_a_num = float('nan')    # Not a Number
```

## Key Properties

- **Immutable:** Cannot change after creation (operations create new floats).
- **Binary representation:** Many familiar decimal fractions cannot be stored exactly.
- **Limited precision:** CPython normally uses IEEE 754 binary64 values (about 15–17 significant decimal digits).
- **Supports arithmetic and comparison operations.**
- **Special values:** Can represent infinity and NaN.

## Common Methods & Functions

- `float(x)`: Convert value to float.
- `.is_integer()`: Check if float is whole number.
- `.as_integer_ratio()`: Exact fraction representation.
- `.hex()`, `.fromhex()`: Hexadecimal representation.
- Math operations: `+`, `-`, `*`, `/`, `//`, `%`, `**`, etc.
- Built-ins: `round()`, `abs()`, `pow()`, `divmod()`

## Examples

```python
# Arithmetic with floats
a = 2.5
b = 1.1
print(a + b)       # 3.6
print(a / b)       # 2.272727...

# Type conversion
num = float("6.28")    # 6.28
val = float(7)         # 7.0

# Special values
print(float('inf') > 1e10)   # True

# Checking if float is whole number
x = 5.0
print(x.is_integer())  # True

# Compare calculated floats with a tolerance
import math
print(math.isclose(0.1 + 0.2, 0.3))  # True
```

## Tips & Common Mistakes

- **Precision errors:**  
  Some decimal fractions can't be represented exactly:
  ```python
  print(0.1 + 0.2)  # 0.30000000000000004
  ```
  Use `round()` for display or `math.isclose()` for approximate comparisons.

- **String conversion:**  
  `float("10.5")` works, but `float("ten")` raises a ValueError.

- **Integer division:**  
  `/` always returns a float (even with integer inputs).

- **NaN and Infinity:**  
  NaN is not equal to itself. Use `math.isnan(value)` to test for it rather than `value == float('nan')`.

- **Money:**
  Use `decimal.Decimal` when values must follow exact decimal arithmetic rules.

- **Do not use floats as dict keys if you need exact matching:**  
  Due to rounding errors, avoid using floats as keys unless you are careful.

## See Also

- [`int`](int)
- [`complex`](complex)
- [`str`](str)
- [`round()`](round)
- [`math`](math)
