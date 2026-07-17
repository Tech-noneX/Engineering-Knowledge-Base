---
id: pop
title: 'pop()'
section: 'List Methods'
module: 'built-in'
subscription: free
difficulty: beginner
reference: 'Removes and returns item at given index (default last) from a list'
tags: ['list', 'method', 'remove', 'return', 'index', 'mutable']
see_also: ['append()', 'remove()', 'del', 'pop() last item **R.W.E**']
works_with: ['list']
file_path: Python-reference/docs/lists/methods/pop_method.md
---

# pop()

- **Used with:** list
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (acts on a single item)
- **Time Complexity:** O(1) for last item, O(n) for index (n = number of elements)

## Description

Removes and returns the item at the given index from a list. If no index is specified, removes and returns the last item.  
Modifies the original list and returns the removed value.  
Raises `IndexError` if the list is empty or the index is out of range.

## Usable With

Lists only. Works on mutable lists (not strings, tuples, or sets).

## Syntax

```python
list.pop([index])
```

- **explanation:**
  - `index` (optional): position to remove and return. Defaults to last item (`-1`).

## Arguments

- **Required:** 0
- **Optional:** 1 (`index`, int)
- **Maximum:** 1

- Required:

```python
numbers = [1, 2, 3]
item = numbers.pop()   # removes and returns 3
```

- Optional:

```python
letters = ['a', 'b', 'c', 'd']
item = letters.pop(1)  # removes and returns 'b'
```

- Maximum

```python
data = [10, 20, 30]
item = data.pop(-2)    # removes and returns 20
```

## Examples

- **Remove last item**

```python
nums = [10, 20, 30]
removed = nums.pop()
# removed is 30, nums is now [10, 20]
```

- **Remove item at specific index**

```python
words = ['cat', 'dog', 'bird']
removed = words.pop(0)
# removed is 'cat', words is now ['dog', 'bird']
```

- **Handle empty list (IndexError)**

```python
lst = []
try:
    lst.pop()
except IndexError:
    print("Cannot pop from empty list!")
```

**Note:**  
If the index is out of range, `IndexError` is raised. Use `try/except` to handle this safely.

## Tips & Common mistakes

- `pop()` both removes **and** returns the item (unlike `del` which just removes).
- O(1) for the last item, but O(n) for removing elsewhere in the list.
- Only works on lists—not strings, tuples, or sets.
- Don’t forget: modifying a list while iterating can cause logic errors.

```python
stack = [1, 2, 3]
while stack:
    print(stack.pop())
# prints 3, then 2, then 1
```

## See Also

- `append()`
- `remove()`
- `del`
- `pop() last item` **R.W.E**
