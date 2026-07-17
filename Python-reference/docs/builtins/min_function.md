---
id: min
title: "min()"
section: "Built-in Functions"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Returns the smallest item in an iterable or among given values"
tags: ["built-in", "function", "minimum", "iterable", "comparison", "numeric", "string"]
see_also: ["max()", "sorted()", "sum()", "min() slowest response"]
works_with: ["list", "tuple", "str", "set", "dict", "iterable"]
file_path: Python-reference/docs/builtins/min_function.md
---

# min()

- **Used with:** Any iterable (list, tuple, string, set, dict, etc.), or two or more arguments
- **Construct:** function
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(n) (n = number of elements)

## Description

The `min()` function returns the smallest item in an iterable or the smallest of two or more arguments. If an iterable is empty and no default value is provided, it raises a `ValueError`. You can also pass a `key` function to control how values are compared.

## Usable With

Use `min()` with lists, tuples, sets, strings, dictionaries (to find the minimum key), or pass multiple arguments directly. Works with numbers, strings, or any comparable objects.

## Syntax

```python
min(iterable, *[, key, default])
min(arg1, arg2, *args[, key])
```

- **explanation:** Call `min()` with an iterable or with two or more arguments. Optional `key` allows custom sorting. Optional `default` is used if the iterable is empty.

## Arguments

- **Required:**
  - 1 iterable **or** 2+ arguments to compare
- **Optional:**
  - `key` (function): a function to customize comparison
  - `default` (any): value to return if the iterable is empty (only allowed with iterables)
- **Maximum:** Unlimited positional arguments or 1 iterable + 2 keyword arguments

```python
# With an iterable
nums = [4, 2, 8, 6]
print(min(nums))  # 2

# With multiple arguments
print(min(4, 2, 8, 6))  # 2

# With key
words = ["apple", "banana", "pear"]
print(min(words, key=len))  # "pear"

# With default
empty = []
print(min(empty, default="No items"))  # "No items"
```

## Examples

- **Find minimum value in a list**

```python
prices = [15.99, 23.50, 9.99]
print(min(prices))  # Output: 9.99
```

- **Get the alphabetically first string**

```python
letters = ["b", "a", "c"]
print(min(letters))  # Output: "a"
```

- **Use key to find the shortest string**

```python
names = ["Eve", "Bob", "Alice"]
print(min(names, key=len))  # Output: "Eve"
```

- **Use default with empty iterable**

```python
items = []
print(min(items, default="empty"))  # Output: "empty"
```

**Note:** Passing an empty iterable with no default raises a `ValueError`.

## Tips & Common mistakes

- Passing an empty iterable without `default` causes a `ValueError`.
- Use `key` for custom comparisons (e.g., by length, absolute value, etc.).
- For dictionaries, `min(d)` returns the minimum key. To get the minimum value: `min(d.values())`.
- If comparing different types (e.g., int and str), `TypeError` will be raised.

```python
# Custom comparison
nums = [-3, 2, -5, 7]
print(min(nums, key=abs))  # -3 (smallest absolute value is 2, so result is 2)
```

## See Also

- [`max()`](max)
- [`sorted()`](sorted)
- [`sum()`](sum)
- [`min() slowest response` **R.W.E**](min_rwe)
