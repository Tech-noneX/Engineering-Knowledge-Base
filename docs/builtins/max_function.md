---
id: max
title: "max()"
section: "Built-in Functions"
module: "build-in"
difficulty: beginner
subscription: free
reference: "Returns the largest item in an iterable or among given values"
tags: ["built-in", "function", "maximum", "iterable", "comparison", "numeric", "string"]
see_also: ["min()", "sorted()", "sum()", "max() top performer"]
works_with: ["list", "tuple", "str", "set", "dict", "iterable"]
---

# max()

- **Used with:** Any iterable (list, tuple, string, set, dict, etc.), or two or more arguments
- **Construct:** function
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(n) (n = number of elements)

## Description

The `max()` function returns the largest item in an iterable or the largest of two or more arguments. If the iterable is empty and no default value is provided, it raises a `ValueError`. You can also pass a `key` function to control how values are compared.

## Usable With

Use `max()` with lists, tuples, sets, strings, dictionaries (to find the maximum key), or pass multiple arguments directly. Works with numbers, strings, or any comparable objects.

## Syntax

```python
max(iterable, *[, key, default])
max(arg1, arg2, *args[, key])
```

- **explanation:** Call `max()` with an iterable or with two or more arguments. Optional `key` allows custom sorting. Optional `default` is used if the iterable is empty.

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
print(max(nums))  # 8

# With multiple arguments
print(max(4, 2, 8, 6))  # 8

# With key
words = ["apple", "banana", "pear"]
print(max(words, key=len))  # "banana"

# With default
empty = []
print(max(empty, default="No items"))  # "No items"
```

## Examples

- **Find maximum value in a list**

```python
prices = [15.99, 23.50, 9.99]
print(max(prices))  # Output: 23.50
```

- **Get the alphabetically last string**

```python
letters = ["b", "a", "c"]
print(max(letters))  # Output: "c"
```

- **Use key to find the longest string**

```python
names = ["Eve", "Bob", "Alice"]
print(max(names, key=len))  # Output: "Alice"
```

- **Use default with empty iterable**

```python
items = []
print(max(items, default="empty"))  # Output: "empty"
```

**Note:** Passing an empty iterable with no default raises a `ValueError`.

## Tips & Common mistakes

- Passing an empty iterable without `default` causes a `ValueError`.
- Use `key` for custom comparisons (e.g., by length, absolute value, etc.).
- For dictionaries, `max(d)` returns the maximum key. To get the maximum value: `max(d.values())`.
- If comparing different types (e.g., int and str), `TypeError` will be raised.

```python
# Custom comparison
nums = [-3, 2, -5, 7]
print(max(nums, key=abs))  # 7 (largest absolute value)
```

## See Also

- `min()`
- `sorted()`
- `sum()`
- `max() top performer` **R.W.E**
