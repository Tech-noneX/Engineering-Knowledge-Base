---
id: len
title: "len()"
section: "Built-in Functions"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Returns the number of items in a sequence or collection"
tags: ["built-in", "function", "length", "size", "iterable", "collection"]
see_also: ["list", "tuple", "str", "dict", "sum()", "len() input validation"]
works_with: ["list", "tuple", "str", "dict", "set", "range", "iterable"]
---

# len()

- **Used with:** Strings, lists, tuples, sets, dictionaries, ranges, bytes, most collections
- **Construct:** function
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(1) for built-in types

## Description

The `len()` function returns the number of items in an object. It works with most built-in Python collections and types, including strings, lists, tuples, sets, dictionaries, ranges, and more. For dictionaries, `len()` returns the number of keys.

## Usable With

Use `len()` to check the size of sequences (strings, lists, tuples), collections (sets, dictionaries), or custom objects that define a `__len__` method.

## Syntax

```python
len(object)
```

- **explanation:** Pass any sequence or collection to `len()` to get the count of items.

## Arguments

- **Required:** 1 (`object`: the collection or sequence whose length you want)
- **Optional:** 0
- **Maximum:** 1

```python
# String length
name = "Python"
print(len(name))  # 6

# List length
nums = [1, 2, 3]
print(len(nums))  # 3

# Dictionary length (number of keys)
data = {"a": 1, "b": 2}
print(len(data))  # 2
```

## Examples

- **Get the length of a string**

```python
msg = "hello"
print(len(msg))  # Output: 5
```

- **Find the number of items in a list**

```python
items = [10, 20, 30, 40]
print(len(items))  # Output: 4
```

- **Check dictionary size (number of keys)**

```python
grades = {"math": 90, "english": 85}
print(len(grades))  # Output: 2
```

- **Works with sets, tuples, ranges**

```python
unique = set([1, 2, 3, 3])
print(len(unique))  # Output: 3

tup = (4, 5, 6)
print(len(tup))  # Output: 3

rng = range(10)
print(len(rng))  # Output: 10
```

**Note:** If the object does not define a length, `TypeError` is raised.

## Tips & Common mistakes

- Only pass objects that are sequences, collections, or define a `__len__` method.
- `len()` returns the number of **top-level** elements only (not nested).
- Does **not** work on numbers or objects without a defined length.

```python
# Common error
# print(len(5))  # TypeError: object of type 'int' has no len()
```

## See Also

- [`list`](list)
- [`tuple`](tuple)
- [`str`](str)
- [`dict`](dict)
- [`sum()`](sum)
- [`len() input validation` **R.W.E**](len_rwe)
