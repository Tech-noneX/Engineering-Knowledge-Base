---
id: reverse
title: 'reverse()'
section: 'List Methods'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Reverses the elements of a list in place'
tags: ['list', 'method', 'reverse', 'in-place', 'mutable', 'order']
see_also: ['reversed()', 'sort()', 'slicing', 'reverse() string **R.W.E**']
works_with: ['list']
file_path: Python-reference/docs/lists/methods/reverse_method.md
---

# reverse()

- **Used with:** list
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (operates in place)
- **Time Complexity:** O(n), where n = number of items in the list

## Description

The `reverse()` method reverses the items of a list **in place** (modifies the original list, no copy).  
Returns `None`.  
Efficient for changing order, but remember: it only works on lists.

## Usable With

Lists only (not strings, tuples, or sets).  
Call on a list to reverse its order.

## Syntax

```python
list.reverse()
```

- **explanation:**  
  - No arguments.  
  - Reverses the list in place; returns `None`.

## Arguments

- **Required:** 0

- **Optional:** 0

- **Maximum:** 0

- Required:

```python
nums = [1, 2, 3]
nums.reverse()
# nums is now [3, 2, 1]
```

- Optional:

```python
# No optional arguments
```

- Maximum

```python
# Only works on lists, no arguments accepted
```

## Examples

- **Reverse a list in place**

```python
colors = ['red', 'green', 'blue']
colors.reverse()
# colors is now ['blue', 'green', 'red']
```

- **Returns None, not the reversed list**

```python
nums = [1, 2, 3]
result = nums.reverse()
print(result)  # prints None
```

- **Reverse twice to restore original order**

```python
lst = [1, 2, 3]
lst.reverse()
lst.reverse()
# lst is back to [1, 2, 3]
```

**Note:**  
For a reversed copy, use `reversed(list)` or slicing: `list[::-1]`.

## Tips & Common mistakes

- Works **only** on lists (not tuples or strings).
- Modifies the list in place—original is changed!
- Does **not** return the reversed list; returns `None`.
- For a non-mutating reverse, use `reversed(list)` or `list[::-1]`.

```python
lst = [1, 2, 3]
print(list(reversed(lst)))  # [3, 2, 1]
print(lst[::-1])            # [3, 2, 1]
```

## See Also

- [`reversed()`](reversed)
- [`sort()`](sort)
- [`slicing`](slicing)
- [`reverse() string` **R.W.E**](reverse_rwe)
