---
id: filter
title: 'filter()'
section: 'Built-in Functions'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Filters elements of an iterable, keeping only those for which a function returns True'
tags: ['built-in', 'function', 'filter', 'iterator', 'condition', 'iterable']
see_also: ['map()', 'list()', 'comprehension', 'filter() with lambda **R.W.E**']
works_with: ['list', 'tuple', 'str', 'set', 'range', 'iterable']
file path: 'docs\builtins\filter_function.md'
---

# filter()

- **Used with:** Any iterable (list, tuple, set, etc.) and a function
- **Construct:** function (returns an iterator)
- **Library:** Built-in
- **Iterable:** Yes (returns an iterator)
- **Time Complexity:** O(n), where n = length of iterable

## Description

The `filter()` function applies a function to each item in an iterable and returns an iterator containing only the items for which the function returns `True`.  
Commonly used for selecting or filtering data based on conditions.  
Wrap in `list()` to get a list of results.

## Usable With

Use with any function that takes a single argument and returns a boolean, plus any iterable (list, tuple, set, string, etc.).

## Syntax

```python
filter(function, iterable)
```

- **explanation:**  
  - `function`: Function that returns `True` or `False` for each item (can use `None` for identity test).
  - `iterable`: Any iterable to filter.
  - Returns an iterator with items where `function(item)` is `True`.

## Arguments

- **Required:** 2 (`function`, `iterable`)

- **Optional:** 0

- **Maximum:** 2

- Required:

```python
def is_even(x):
    return x % 2 == 0

nums = [1, 2, 3, 4]
evens = filter(is_even, nums)  # iterator of 2, 4
```

- Optional:

```python
# function can be None (keeps items that are true in a boolean context)
data = ['', 'hi', None, 'bye']
filtered = filter(None, data)
# filtered yields 'hi', 'bye'
```

- Maximum

```python
# Only two arguments allowed: function and iterable
```

## Examples

- **Filter even numbers with a function**

```python
nums = [1, 2, 3, 4]
evens = list(filter(lambda x: x % 2 == 0, nums))
# evens is [2, 4]
```

- **Filter truthy values with None**

```python
data = ['', 'apple', None, 'banana']
result = list(filter(None, data))
# result is ['apple', 'banana']
```

- **Filter words by length**

```python
words = ['hi', 'hello', 'a', 'world']
long_words = list(filter(lambda w: len(w) > 2, words))
# long_words is ['hello', 'world']
```

**Note:**  
`filter()` returns an iterator—wrap in `list()` or use a loop to access results.

## Tips & Common mistakes

- Use `list(filter(...))` to get a list result in Python 3.
- `function` must return `True` or `False`; use lambdas for quick, custom logic.
- List comprehensions are often clearer and more Pythonic for simple filtering.
- Using `None` as the function keeps only "truthy" items.

```python
nums = [0, 1, 2, '', None, 3]
filtered = list(filter(None, nums))
# filtered is [1, 2, 3]
```

## See Also

- [`map()`](map)
- [`list()`](list)
- [`comprehension`](comprehension)
- [`filter() with lambda` **R.W.E**](filter_rwe)
