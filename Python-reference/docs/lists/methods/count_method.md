---
id: count
title: 'count()'
section: 'List Methods'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Returns the number of times a value appears in a list'
tags: ['list', 'method', 'count', 'search', 'value', 'frequency']
see_also: ['index()', 'len()', 'collections.Counter', 'count() all types **R.W.E**']
works_with: ['list']
file_path: Python-reference/docs/lists/methods/count_method.md
---

# count()

- **Used with:** list
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (returns a number, does not iterate for you)
- **Time Complexity:** O(n), where n = number of items in the list

## Description

The `count()` method returns the number of times a specified value appears in a list.  
Useful for finding duplicates, checking frequency, or simple data analysis.

## Usable With

Lists only (also works on strings and tuples, but this card is for list usage).

## Syntax

```python
list.count(value)
```

- **explanation:**  
  - `value`: The item to count (required).  
  - Returns the number of times `value` appears in the list.

## Arguments

- **Required:** 1 (`value`)

- **Optional:** 0

- **Maximum:** 1

- Required:

```python
nums = [1, 2, 2, 3, 2]
nums.count(2)  # returns 3
```

- Optional:

```python
# No optional arguments; only value is required
```

- Maximum

```python
# Only one argument allowed (the value)
```

## Examples

- **Count occurrences in a list**

```python
colors = ['red', 'blue', 'red', 'green', 'red']
red_count = colors.count('red')
# red_count is 3
```

- **Count a value not present (returns 0)**

```python
words = ['hello', 'world']
words.count('hi')  # returns 0
```

- **Count booleans or numbers**

```python
data = [True, False, True, True]
true_count = data.count(True)
# true_count is 3
```

**Note:**  
The search is linear; use `collections.Counter` for large lists or many values.

## Tips & Common mistakes

- `count()` only counts exact matches (`==`), not similar or partial matches.
- Use for simple cases—`Counter` is more efficient for counting many items.
- Works on lists, tuples, and strings (but not on sets or dicts).
- Returns `0` if the value is not found (no error).

```python
nums = [1, 1, 2, 3]
from collections import Counter
Counter(nums)
# Counter({1: 2, 2: 1, 3: 1})
```

## See Also

- `index()`
- `len()`
- `collections.Counter`
- `count() all types` **R.W.E**
