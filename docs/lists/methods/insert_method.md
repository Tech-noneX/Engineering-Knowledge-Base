---
id: insert
title: "insert()"
section: "List Methods"
tags: ["list", "method", "in-place", "add", "mutable", "position"]
see_also: ["append()", "extend()"]
works_with: ["list"]
---

# insert

- **Used with:**  
lists  
- **Construct:**  
Method  
- **Library:**  
Built-in  
- **Iterable:**  
No (modifies list in place)  
- **Time Complexity:**  
O(n) (worst-case, as elements may be shifted)

## Description

Inserts an item at a given position in the list.  
All items at or after the given index are shifted to the right.  
The method modifies the original list and returns `None`.

## Usable With

Python `list` objects.

## Syntax

```python
list.insert(index, item)
```

- **explanation:**
  - `list`: The list you want to modify.
  - `.insert()`: Method that inserts an element.
  - `index`: The position where you want to insert the item. If negative, counts from the end. If greater than the list length, the item is added at the end.
  - `item`: The element you want to insert at the given index.
  - Returns `None`. List is modified in place.

## Arguments

**Required:** 2 (`index`, `item`)  
**Optional:** 0  
**Maximum:** 2

- Required:

```python
index  # The position in the list to insert at.
item   # The object to insert.
# Example:
numbers = [1, 2, 4]
numbers.insert(2, 3)  # [1, 2, 3, 4]
```

- Optional:

```python
# No optional arguments for insert()
```

- Maximum

```python
# Must always provide index and item.
# Example:
letters = ['a', 'c', 'd']
letters.insert(1, 'b')  # ['a', 'b', 'c', 'd']
```

## Examples

- **Insert at a specific index**

```python
numbers = [1, 2, 4]
numbers.insert(2, 3)
# numbers is now [1, 2, 3, 4]
```

- **Insert at the beginning**

```python
letters = ['b', 'c', 'd']
letters.insert(0, 'a')
# letters is now ['a', 'b', 'c', 'd']
```

- **Insert at the end (index > length)**

```python
fruits = ['apple', 'banana']
fruits.insert(10, 'cherry')
# fruits is now ['apple', 'banana', 'cherry']
```

- **Insert with negative index (from the end)**

```python
data = [0, 1, 2]
data.insert(-1, 99)
# data is now [0, 1, 99, 2]
```

 **Note:**

- The original list is always modified.
- If `index` is larger than the length of the list, `item` is appended at the end.
- If `index` is negative, it is treated as `len(list) + index`.

## Tips & Common mistakes

- Remember: `insert()` returns `None`, not the new list.
- If you use an index greater than the list length, item is added at the end.
- Negative indices can be used for insertion, but may be confusing—test first.
- For adding to the end, `append()` is faster and clearer.
- Frequent insertions at the beginning or middle of large lists can be slow (O(n) time).

```python
# Incorrect: expecting insert() to return the list!
nums = [1, 2]
result = nums.insert(1, 5)
print(result)  # Output: None
```

## See Also

- `append()`
- `extend()`
