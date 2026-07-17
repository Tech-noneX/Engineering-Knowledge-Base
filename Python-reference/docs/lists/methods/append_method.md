---
id: append
title: "append()"
section: "List Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Adds a single item to the end of a list in place"
tags: ["list", "method", "in-place", "add", "mutable"]
see_also: ['add()', 'extend()', 'insert()', 'pop()', "append() build shopping cart **R.W.E**"]
works_with: ['list'] 
file_path: Python-reference/docs/lists/methods/append_method.md
---

# append()

- **Used with:**
  List
- **Construct:**
  Method
- **Library:**
  Built-in
- **Iterable:**
  Yes (but only on lists; argument itself can be any object)
- **Time Complexity:**
  Average: O(1) (amortized constant time)

## Description

`append()` is a built-in list method that adds a single element to the end of the list. It modifies the original list in place and always returns `None`. Only one argument can be added per call. The element can be any object—string, number, another list, dict, etc.  
**Common use:** Grow a list by adding new items to its end during loops or dynamic operations.

## Usable With

- Lists only (not tuples, sets, dicts, or strings)

## Syntax

```python
list.append(element)
```

## Arguments

**Required:**

- `element` (any type): The item to add at the end of the list.

**Optional:**

- None.

**Maximum:**

- Only one argument allowed (besides self).

- Required:

```python
fruits = ["apple", "banana"]
fruits.append("cherry")  # adds "cherry"
```

- Optional:

```python
# append() does not take optional arguments
```

- Maximum

```python
# only 1 element at a time
```

## Examples

- **Basic append**

```python
numbers = [1, 2, 3]
numbers.append(4)
# numbers = [1, 2, 3, 4]
```

- **Appending a list as a single element**

```python
lst = [1, 2]
lst.append([3, 4])
# lst = [1, 2, [3, 4]]
```

- **Appending any data type**

```python
data = []
data.append("hello")
data.append(42)
data.append({"a": 1})
# data = ["hello", 42, {"a": 1}]
```

 **Note:**  
The `append()` method always modifies the original list. It does **not** return a new list, and always returns `None`.

## Tips & Common mistakes

- `append()` can only add one item per call.  
- To add multiple items, use `extend()` or a loop.  
- `append()` does **not** return the new list (it returns `None`).  
- Appending a list does **not** merge—results in a nested list.

```python
# Wrong way (returns None)
result = mylist.append(5)
# result is None, mylist is updated

# Correct way:
mylist.append(5)
```

## See Also

- [`extend()`](extend)
- [`add()`](add)
- [`insert()`](insert)
- [`pop()`](pop)
- [`append() build shopping cart` **R.W.E**](append_rwe)
