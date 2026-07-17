---
id: index
title: "index()"
section: "List Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Returns the index of the first occurrence of a value in a sequence"
tags: ["list", "tuple", "string", "method", "search", "sequence"]
see_also: ["find()", "count()", "pop()", "enumerate()", "index() error handling **R.W.E**"]
works_with: ["list", "tuple", "string"]
file_path: Python-reference/docs/lists/methods/index_method.md
---

# index

- **Used with:**  
lists, strings, tuples  
- **Construct**
Method
- **Library**
Built-in  
- **Iterable:**  
Yes  
- **Time Complexity:**  
O(n) (worst case, scans up to the end of the sequence)

## Description

Returns the first index of the specified value in the sequence.  
Searches the sequence from the beginning (or from the optional start index) to the end (or up to, but not including, the optional stop index).  
Raises `ValueError` if the value is not found.

## Usable With

Python `list`, `str`, and `tuple` objects.

## Syntax

```python
sequence.index(value, start=0, stop=len(sequence))
```

- **explanation:**
  - `sequence`: The list, tuple, or string to search.
  - `.index()`: Method to find the first occurrence of a value.
  - `value`: The item to search for (required).
  - `start=0`: (Optional) The position to start searching (defaults to 0, the beginning).
  - `stop=len(sequence)`: (Optional) The position to stop searching (defaults to the end of the sequence).
  - Returns the index of the first occurrence of `value` within the specified range.
  - Raises `ValueError` if `value` is not found.

## Arguments

- **Required:** 1 (`value`)  
- **Optional:** 2 (`start`, `stop`)  
- **Maximum:** 3

- Required:

```python
value  # The value to search for.
# Example:
[10, 20, 30, 20].index(20)  # returns 1
```

- Optional:

```python
start  # (Optional) The index to start searching from.
# Example:
[10, 20, 30, 20].index(20, 2)  # returns 3

stop   # (Optional) The index to stop searching (non-inclusive).
# Example:
[10, 20, 30, 20].index(20, 0, 2)  # returns 1
```

- Maximum

```python
# Using all arguments:
data = [1, 2, 3, 2, 4]
data.index(2, 2, 5)  # returns 3 (searches from index 2 to 4)
```

## Examples

- **Find index of a value in a list**

```python
numbers = [10, 20, 30, 20]
idx = numbers.index(20)
# idx is 1
```

- **Find index after a certain position**

```python
numbers = [10, 20, 30, 20]
idx = numbers.index(20, 2)
# idx is 3
```

- **Find index within a range**

```python
letters = ['a', 'b', 'c', 'b']
idx = letters.index('b', 2)
# idx is 3
```

- **Find index in a string**

```python
text = "banana"
pos = text.index('a')
# pos is 1
```

- **Find index with start and stop**

```python
numbers = [1, 2, 3, 2, 5]
idx = numbers.index(2, 2, 5)
# idx is 3
```

 **Note:**

- If the value does not exist in the specified range, a `ValueError` is raised.
- Only the first occurrence is found, even if there are multiple.

## Tips & Common mistakes

- **Raises `ValueError`** if the value is not found—wrap in `try/except` if unsure.
- Only returns the first match; to find all, use a loop or list comprehension.
- Works for lists, tuples, and strings with identical syntax.
- `start` and `stop` are **inclusive** of `start`, **exclusive** of `stop`.
- Negative indices are supported.

```python
# Handling missing value:
nums = [1, 2, 3]
try:
    idx = nums.index(4)
except ValueError:
    idx = -1  # or handle error as needed
```

## See Also

- `find()`
- `count()`
- `pop()`
- `index() error handling` **R.W.E**
