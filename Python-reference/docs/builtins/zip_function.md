---
id: zip
title: 'zip()'
section: 'Built-in Functions'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Combines iterables element-wise into tuples, with optional length checking'
tags: ['built-in', 'function', 'zip', 'combine', 'iterator', 'tuple', 'parallel']
see_also: ['enumerate()', 'map()', 'list()', 'dict()', 'zip() real-world pairing **R.W.E**']
works_with: ['list', 'tuple', 'str', 'set', 'range', 'iterable', 'sequence']
file_path: Python-reference/docs/builtins/zip_function.md
---

# zip()

- **Used with:** Iterables (lists, tuples, strings, sets, etc.)
- **Construct:** function (returns an iterator)
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(n), where n is the length of the shortest input

## Description

The `zip()` function takes zero or more iterables (like lists, tuples, or strings) and returns an iterator of tuples. Each tuple contains the items from the same position in each input. By default, `zip()` stops when the shortest input is exhausted.
Commonly used to combine data, loop in parallel, or pair items together.

## Usable With

Use `zip()` with any combination of iterables—lists, tuples, strings, sets, ranges, etc. Each tuple in the result contains one element from each input at the same index.

## Syntax

```python
zip(*iterables, strict=False)
```

- **explanation:**  
  - `*iterables`: zero or more iterable objects to combine by position.
  - `strict`: keyword-only argument. When `True`, different input lengths raise `ValueError` instead of silently dropping extra items.
  - Returns an iterator of tuples; convert to a list or loop over it.

## Arguments

- **Required:** 0
- **Optional:** Any number of iterables and the keyword-only `strict` argument
- **Maximum:** No fixed maximum number of iterables

- Required:

```python
a = [1, 2, 3]
b = ['x', 'y', 'z']
z = zip(a, b)  # pairs: (1, 'x'), (2, 'y'), (3, 'z')
```

- Optional:

```python
# zip() works with any number of iterables, not just two
names = ['Tom', 'Sue']
scores = [90, 85]
ids = [101, 102]
zipped = zip(names, scores, ids)
```

- Maximum

```python
# zip() supports unlimited iterables; stops at shortest
a = [1, 2, 3]
b = [4, 5]
c = [6, 7, 8]
print(list(zip(a, b, c)))  # [(1, 4, 6), (2, 5, 7)]
```

- Strict length checking:

```python
names = ["Ada", "Linus"]
scores = [95, 88]
print(list(zip(names, scores, strict=True)))
# [('Ada', 95), ('Linus', 88)]
```

## Examples

- **Pair items from two lists**

```python
names = ['Anna', 'Bob']
scores = [8, 9]
for name, score in zip(names, scores):
    print(name, score)
# Output:
# Anna 8
# Bob 9
```

- **Convert zipped pairs to a list or dict**

```python
ids = [1, 2, 3]
letters = ['a', 'b', 'c']
paired = list(zip(ids, letters))
# paired is [(1, 'a'), (2, 'b'), (3, 'c')]

mapping = dict(zip(ids, letters))
# mapping is {1: 'a', 2: 'b', 3: 'c'}
```

- **Unzip with * operator**

```python
pairs = [(1, 'a'), (2, 'b')]
nums, chars = zip(*pairs)
# nums = (1, 2), chars = ('a', 'b')
```

**Note:**  
If the iterables are different lengths, `zip()` stops at the shortest.  
Use `itertools.zip_longest()` if you want to fill missing values.
Use `strict=True` when different lengths would indicate a bug. The `strict`
argument was added in Python 3.10.

## Tips & Common mistakes

- Result is an **iterator**; convert to a list to reuse or index.
- Stops at the shortest input by default; use `strict=True` to detect mismatched lengths.
- To "unzip," use the unpacking operator: `zip(*zipped)`.
- Use with any number of iterables (not just two).
- `zip()` with no inputs produces an empty iterator; one input produces 1-item tuples.

```python
# zip() with 3 iterables, convert to list
result = list(zip([1, 2], [3, 4], [5, 6]))
# Output: [(1, 3, 5), (2, 4, 6)]
```

## See Also

- [`enumerate()`](enumerate)
- [`map()`](map)
- [`list()`](list)
- [`dict()`](dict)
- [`zip() real-world pairing` **R.W.E**](zip_rwe)
