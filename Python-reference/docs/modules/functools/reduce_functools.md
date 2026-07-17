---
id: reduce
title: "reduce()"
section: "Modules functools"
module: 'functools'
difficulty: intermediate
subscription: premium
reference: "Cumulatively applies a function to items in an iterable, reducing to a single value"
tags: ["standard library", "function", "reduce", "iteration", "functools", "aggregation", "fold"]
see_also: ["sum()", "map()", "filter()", "functools", "reduce() invoice total calculation **R.W.E**"]
works_with: ["list", "tuple", "set", "iterable"]
file_path: Python-reference/docs/modules/functools/reduce_functools.md
---

# reduce()

- **Used with:** Iterables (lists, tuples, sets, etc.)
- **Construct:** function (from `functools` module)
- **Library:** `functools` (not built-in by default)
- **Iterable:** Yes
- **Time Complexity:** O(n) (n = number of elements)

## Description

The `reduce()` function repeatedly applies a function to the elements of an iterable, reducing the iterable to a single cumulative value. Common for mathematical operations (product, sum, max, etc.) and aggregation. Returns a single result. Must be imported from the `functools` module in Python 3+.

## Usable With

Use `reduce()` with any iterable and a function that takes two arguments. Most commonly used with lists or tuples of numbers, but can be used with any data type and custom aggregation function.

## Syntax

```python
from functools import reduce

reduce(function, iterable)
reduce(function, iterable, initial)
```

- **explanation:**  
  - `function`: a function taking two arguments, applied cumulatively.
  - `iterable`: items to process.
  - `initial` (optional): starting value; if given, it is placed before the iterable's items and is returned when the iterable is empty.

## Arguments

- **Required:** 2 (`function`, `iterable`)
- **Optional:** 1 (`initial`, any type)
- **Maximum:** 3

```python
from functools import reduce

# Sum a list
nums = [1, 2, 3, 4]
total = reduce(lambda x, y: x + y, nums)  # 10

# With initializer
total = reduce(lambda x, y: x + y, nums, 5)  # 15
```

Python 3.14+ also accepts `initial` as a keyword argument:

```python
total = reduce(lambda x, y: x + y, [], initial=0)
print(total)  # 0
```

## Examples

- **Multiply all numbers in a list**

```python
from functools import reduce
import operator

numbers = [2, 3, 4]
result = reduce(operator.mul, numbers)
print(result)  # Output: 24
```

- **Find the maximum value using reduce**

```python
from functools import reduce

values = [7, 2, 10, 4]
max_val = reduce(lambda a, b: a if a > b else b, values)
print(max_val)  # Output: 10
```

- **Sum with initializer**

```python
from functools import reduce

nums = [10, 20, 30]
total = reduce(lambda x, y: x + y, nums, 100)
print(total)  # Output: 160
```

**Note:** If the iterable is empty and no `initial` value is provided, `TypeError` is raised. The `initial` keyword form was added in Python 3.14; pass it positionally on older versions.

## Tips & Common mistakes

- Always import `reduce` from `functools` in Python 3+ (`from functools import reduce`).
- For simple addition or multiplication, prefer `sum()` or `math.prod()` for clarity and performance.
- The function must take exactly **two arguments** and return a result of the same type.
- If the iterable is empty and no `initial` value is provided, a `TypeError` is raised.

```python
# Common error
from functools import reduce
print(reduce(lambda x, y: x + y, []))  # TypeError
```

## See Also

- `sum()`
- `map()`
- `filter()`
- `functools`
- `reduce() invoice total calculation` **R.W.E**
