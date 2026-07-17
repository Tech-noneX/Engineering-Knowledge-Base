---
id: bool
title: bool
section: Data Types
module: built-in
difficulty: beginner
subscription: free
reference: Boolean type; represents True or False values in Python.
tags: ['data type', 'bool', 'boolean', 'logic', 'true', 'false', 'conditional']
see_also: ['int', 'str', 'float', 'None', 'truthy', 'falsy', 'not']
works_with: ['int', 'str', 'list', 'set', 'dict', 'for', 'in']
file_path: Python-reference/docs/data-types/bool_datatype.md
---

# bool

## Description

A **bool** (Boolean) is a built-in type that can only have two possible values: `True` or `False`.  

- Used for logical conditions, comparisons, and control flow.
- The result of comparisons and many built-in functions is a boolean.

Commonly used in `if` statements, loops, filtering, and expressions.

## Usable With

- Used in all conditional statements (`if`, `while`).
- Can be created from numbers, strings, lists, and most objects with `bool()`.
- Works with logical operators: `not`, `and`, `or`.

## Creation & Syntax

```python
# Direct assignment:
flag = True
error = False

# From expressions:
is_even = (x % 2 == 0)

# Using bool() constructor:
val = bool(1)     # True
val = bool(0)     # False
val = bool('')    # False (empty string)
val = bool('hi')  # True (non-empty string)
```

## Key Properties

- **Immutable:** Value cannot be changed after creation.
- **Subclass of int:** `True` == 1, `False` == 0.
- **Used in logic:** Core type for conditions and boolean logic.
- **"Truthy" and "Falsy":** Most values can be converted to `True` or `False` using `bool()`.

## Common Methods & Functions

- `bool(x)`: Convert value to boolean.
- Logical operators: `not`, `and`, `or`.
- Used in functions like `all()`, `any()`, `filter()`.

## Examples

```python
# Basic usage
active = True
if active:
    print("Active!")

# Comparisons
a = 5
print(a > 3)    # True

# Type conversion
print(bool([]))     # False (empty list)
print(bool([1]))    # True (non-empty list)
print(True + 4)     # 5 (True is 1)
print(False * 10)   # 0 (False is 0)
```

## Tips & Common Mistakes

- **Truthy vs Falsy:**  
  Many values evaluate to `False` (empty collections, 0, `None`, `''`); others are `True`.
  
  ```python
  if not my_list:    # Checks if list is empty
      print("Empty!")
  ```

- **Boolean is a subclass of `int`:**
  `True` and `False` behave like `1` and `0` in numeric operations, but they are boolean objects and should normally be used for logic.

  ```python
  sum([True, False, True])   # 2
  ```

- **Don’t compare with `== True` or `== False`:**  
  Use direct checks: `if flag:` or `if not flag:` instead of `if flag == True`.

- **Case-sensitive:**  
  Must be capitalized: `True`/`False` (not `true`/`false`).

- **`and` and `or` may return operands:**
  These operators do not always return a `bool`; they return one of the values they evaluate.

  ```python
  name = "Ada"
  display_name = name or "Anonymous"  # "Ada"
  ```

## See Also

- [`int`](int)
- [`str`](str)
- [`float`](float)
- [`None`](None)
- [`not`](not)
- [`truthy`](truthy)
- [`falsy`](falsy)
