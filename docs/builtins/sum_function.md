---
id: sum
title: "sum()"
section: "Built-in Functions"
module: "build-in"
difficulty: beginner
subscription: free
reference: "Adds up all numeric items in an iterable, with optional start value"
tags: ["built-in", "function", "sum", "numeric", "iterable", "addition"]
see_also: ["min()", "max()", "len()", "reduce()", "sum() total invoice calculation"]
works_with: ["list", "tuple", "set", "dict", "iterable", "range"]
---

# sum()

- **Used with:** Any iterable of numbers (list, tuple, set, dict values, range, etc.)
- **Construct:** function
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(n) (n = number of elements)

## Description

The `sum()` function returns the total of all items in an iterable (such as a list, tuple, set, or range). You can also provide an optional `start` value that is added to the total. The default start is `0`. Items must be numbers (int, float, complex) or support addition.

## Usable With

Use `sum()` with lists, tuples, sets, ranges, and other iterables containing numbers. You can also use it with dictionary values by passing `dict.values()`.

## Syntax

```python
sum(iterable, start=0)
```

- **explanation:** Pass an iterable of numbers to sum. The optional `start` value is added to the total (default is `0`).

## Arguments

- **Required:** 1 (`iterable`: an iterable of numbers)
- **Optional:** 1 (`start`, numeric: initial value to add to the sum)
- **Maximum:** 2

```python
# Add all numbers in a list
nums = [1, 2, 3]
print(sum(nums))  # 6

# Use start value
print(sum(nums, 10))  # 16
```

## Examples

- **Sum a list of numbers**

```python
values = [10, 20, 30]
print(sum(values))  # Output: 60
```

- **Sum a range of numbers**

```python
total = sum(range(1, 6))
print(total)  # Output: 15
```

- **Sum dictionary values**

```python
scores = {"a": 5, "b": 7}
print(sum(scores.values()))  # Output: 12
```

- **Sum with a starting value**

```python
nums = [4, 5, 6]
print(sum(nums, 100))  # Output: 115
```

**Note:** The iterable must contain numbers. Using non-numeric values raises a `TypeError`.

## Tips & Common mistakes

- Passing non-numeric values (e.g., strings) will cause a `TypeError`.
- `sum()` is for **numbers** only. For concatenating strings or sequences, use `"".join()` or `itertools.chain()`.
- For summing nested lists (e.g., matrix rows), use a generator: `sum(sum(row) for row in matrix)`.
- Avoid using `sum()` for large lists of strings; use `"".join()` instead (much faster for strings).

```python
# Error example
# sum(["a", "b", "c"])  # TypeError
```

## See Also

- `min()`
- `max()`
- `len()`
- `reduce()`
- `sum() total invoice calculation` **R.W.E**
