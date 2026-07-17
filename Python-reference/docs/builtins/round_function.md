---
id: round
title: "round()"
section: "Built-in Functions"
module: "built-in"
difficulty: beginner
subscription: premium
reference: "Rounds a number to the nearest integer or specified decimal place"
tags: ["built-in", "function", "round", "float", "decimal", "precision", "number"]
see_also: ["int()", "float()", "math.ceil()", "math.floor()", "round() currency formatting"]
works_with: ["int", "float", "numeric"]
file_path: Python-reference/docs/builtins/round_function.md
---

# round()

- **Used with:** `int`, `float`, numeric values
- **Construct:** function
- **Library:** built-in
- **Iterable:** No
- **Time Complexity:** O(1)

## Description

The `round()` function returns a number rounded to a given number of decimal places. By default, it rounds to the nearest integer. If the optional `ndigits` argument is given, it rounds the number to that many decimal places. Rounding uses "round half to even" (banker's rounding) for halfway cases.

## Usable With

Use `round()` on numbers (integers or floats) when you need to control decimal precision—e.g., for displaying currency, scientific results, or data presentation.

## Syntax

```python
round(number[, ndigits])
```

- **explanation:**  
  - `number` (required): the value to round.  
  - `ndigits` (optional): the number of decimal places to round to. If omitted, rounds to the nearest integer.

## Arguments

- **Required:** 1 (`number`)

- **Optional:** 1 (`ndigits`)

- **Maximum:** 2

- **Required:**

```python
round(3.14159)        # 3
```

- **Optional:**

```python
round(3.14159, 2)     # 3.14
```

- **Maximum:**

```python
round(2.71828, 3)     # 2.718
```

## Examples

- **Round to nearest integer**

```python
result = round(5.7)
print(result)  # Output: 6
```

- **Round to 2 decimal places**

```python
value = 9.8765
print(round(value, 2))  # Output: 9.88
```

- **Banker’s rounding (halfway cases)**

```python
print(round(2.5))  # Output: 2  (2 is even)
print(round(3.5))  # Output: 4  (4 is even)
```

**Note:** For “halfway” cases (e.g., x.5), Python uses **banker's rounding**: rounds to the nearest even number.

## Tips & Common mistakes

- `ndigits` can be negative to round to tens, hundreds, etc.: `round(123, -1)` gives `120`.
- Only works with numbers; using on other types raises `TypeError`.
- Floating-point arithmetic can introduce subtle rounding errors (e.g., `round(2.675, 2)` may give `2.67` due to binary representation).
- For always rounding up or down, use `math.ceil()` or `math.floor()`.

```python
import math
print(math.ceil(2.3))   # 3
print(math.floor(2.7))  # 2
```

## See Also

- [`int()`](int)
- [`float()`](float)
- [`ceil()`](ceil)
- [`floor()`](floor)
- [`round() currency formatting` **R.W.E**](round_rwe)
