---
id: extend
title: "extend()"
section: "List Methods"
tags: ["list", "method", "in-place", "add", "iterable", "mutable"]
---

# extend

**Used with:**  
List
**Construct:**  
Method
**Library:**  
Built-in
**Iterable:**  
Yes (argument must be iterable, e.g. list, tuple, set, string, or a variable referencing any iterable)

**Time Complexity:**  
O(k), where k = number of elements added

## Description

`extend()` is a built-in list method that takes an iterable (like a list, tuple, set, string, etc.) and adds each of its elements to the end of the original list. The argument can be a variable that refers to any iterable, not just a literal.  
**Common use:** Combine or concatenate lists, or add multiple elements to a list in a single operation.

## Usable With

- Lists only (as the object being extended)
- Any iterable (including variables referencing lists, tuples, sets, strings, etc.) as the argument

## Syntax

```python
list.extend(iterable)
```

## Arguments

**Required:**

- `iterable` (any iterable): The items to be added to the end of the list.  
  This can be a literal iterable (e.g. `[3, 4]`) or a variable containing any iterable (such as a list variable).

**Optional:**

- None.

**Maximum:**

- Only one argument (the iterable) besides self.

- Required:

```python
nums = [1, 2]
to_add = [3, 4]
nums.extend(to_add)
# nums = [1, 2, 3, 4]
```

- Optional:

```python
# extend() does not take optional arguments
```

- Maximum

```python
# list.extend(iterable) - only 1 iterable at a time
```

## Examples

- **Extend with another list variable**

```python
a = [1, 2]
more = [3, 4]
a.extend(more)
# a = [1, 2, 3, 4]
```

- **Extend with a tuple**

```python
a = [1, 2]
t = (3, 4)
a.extend(t)
# a = [1, 2, 3, 4]
```

- **Extend with a string**

```python
chars = ['a', 'b']
s = "cd"
chars.extend(s)
# chars = ['a', 'b', 'c', 'd']
```

**Note:**  
The `extend()` method modifies the original list in place and always returns `None`.  
The argument can be a variable referencing any iterable, not just a literal.

## Tips & Common mistakes

- The argument must be **iterable**.  
- Extending with a string adds each character separately.  
- `extend()` is not the same as `append()`—`append()` adds the entire argument as one element; `extend()` iterates and adds each element individually.  
- The argument can be a variable containing a list or any iterable.  
- Does not return a new list—always returns `None`.

```python
# Common mistake: using append instead of extend
lst = [1, 2]
to_add = [3, 4]
lst.append(to_add)
# lst == [1, 2, [3, 4]]  # wrong

lst = [1, 2]
to_add = [3, 4]
lst.extend(to_add)
# lst == [1, 2, 3, 4]    # correct
```
