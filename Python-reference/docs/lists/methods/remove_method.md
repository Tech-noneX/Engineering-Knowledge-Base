---
id: remove
title: 'remove()'
section: 'List Methods'
module: 'built-in'
subscription: free
difficulty: beginner
reference: 'Removes the first occurrence of a value from a list'
tags: ['list', 'method', 'remove', 'value', 'in-place', 'mutable']
see_also: ['pop()', 'del', 'clear()', 'remove() all occurrences **R.W.E**']
works_with: ['list']
file_path: Python-reference/docs/lists/methods/remove_method.md
---

# remove()

- **Used with:** list
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (removes by value, not index)
- **Time Complexity:** O(n), where n is the number of items in the list

## Description

Removes the **first occurrence** of the specified value from the list.  
Modifies the original list and returns `None`.  
Raises a `ValueError` if the value is not found.

## Usable With

Lists only (not strings, tuples, sets, or dicts).

## Syntax

```python
list.remove(value)
```

- **explanation:**  
  - `value` (required): The item to remove. Only the first matching item is removed.

## Arguments

- **Required:** 1 (`value`)

- **Optional:** 0

- **Maximum:** 1

- Required:

```python
nums = [1, 2, 3, 2]
nums.remove(2)   # removes the first 2; nums is now [1, 3, 2]
```

- Optional:

```python
# No optional arguments for remove()
```

- Maximum

```python
# Only one argument allowed: value
```

## Examples

- **Remove first occurrence of a value**

```python
items = ['apple', 'banana', 'apple']
items.remove('apple')
# items is now ['banana', 'apple']
```

- **Remove an item not in the list (raises ValueError)**

```python
lst = [1, 2, 3]
try:
    lst.remove(99)
except ValueError:
    print("Value not found!")
```

- **Remove in a loop (removes first matching each time)**

```python
data = [2, 2, 2]
while 2 in data:
    data.remove(2)
# data is now []
```

**Note:**  
Only the **first** matching item is removed. For all occurrences, use a loop or list comprehension.

## Tips & Common mistakes

- `remove()` returns `None`, not the removed value.
- Raises `ValueError` if the value is not found—handle with `try/except` if unsure.
- Use a loop or list comprehension to remove **all** occurrences.
- Only works with lists (not tuples, sets, or dicts).

```python
nums = [1, 2, 2, 3]
for n in nums:
    if n == 2:
        nums.remove(n)
print(nums)  # Output: [1, 2, 3]  (not all 2s are removed!)
```

- Why this is a mistake:
  - When you remove an item from a list while iterating, Python changes the list length, which causes some elements to be skipped.

  - Many beginners expect all `2`s to be removed, but only the first occurrence and every other matching value will be skipped!

## See Also

- [`pop()`](pop)
- [`del`](del)
- [`clear()`](clear)
- [`remove() all occurrences` **R.W.E**](remove_rwe)
