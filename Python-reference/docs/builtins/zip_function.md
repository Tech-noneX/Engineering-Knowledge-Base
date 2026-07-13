---
id: zip
title: 'zip()'
section: 'Built-in Functions'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Combines multiple iterables element-wise into tuples'
tags: ['built-in', 'function', 'zip', 'combine', 'iterator', 'tuple', 'parallel']
see_also: ['enumerate()', 'map()', 'list()', 'dict()', 'zip() real-world pairing **R.W.E**']
works_with: ['list', 'tuple', 'str', 'set', 'range', 'iterable', 'sequence']
file path: 'docs\builtins\zip_function.md'
---

# zip()

- **Used with:** Iterables (lists, tuples, strings, sets, etc.)
- **Construct:** function (returns an iterator)
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(n), where n is the length of the shortest input

## Description

The `zip()` function takes two or more iterables (like lists, tuples, strings) and returns an iterator of tuples, where each tuple contains the elements from each iterable at the same position. Stops when the shortest input is exhausted.  
Commonly used to combine data, loop in parallel, or pair items together.

## Usable With

Use `zip()` with any combination of iterables—lists, tuples, strings, sets, ranges, etc. Each tuple in the result contains one element from each input at the same index.

## Syntax

```python
zip(iterable1, iterable2, ...)
```

- **explanation:**  
  - Pass two or more iterables to combine their elements by index.
  - Returns an iterator of tuples; convert to a list or loop over it.

## Arguments

- **Required:** 2 or more iterables
- **Optional:** Unlimited (as many iterables as you want)
- **Maximum:** Unlimited

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

## Tips & Common mistakes

- Result is an **iterator**; convert to a list to reuse or index.
- Stops at the shortest input—no error or filling!
- To "unzip," use the unpacking operator: `zip(*zipped)`.
- Use with any number of iterables (not just two).

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
