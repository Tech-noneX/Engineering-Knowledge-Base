---
id: enumerate
title: "enumerate()"
section: "Built-in Functions"
module: "built-in"
difficulty: beginner 
subscription: premium
reference: "Adds index to each item when looping over an iterable"
tags: ["built-in", "function", "enumerate", "loop", "index", "iterator", "for"]
see_also: ["zip()", "range()", "list()", "for", "enumerate() quiz generator"]
works_with: ["list", "tuple", "str", "set", "iterable", "sequence"]
file_path: Python-reference/docs/builtins/enumerate_function.md
---

# enumerate()

- **Used with:** Iterables (lists, tuples, strings, sets, etc.)
- **Construct:** function (returns an enumerate object)
- **Library:** built-in
- **Iterable:** Yes
- **Time Complexity:** O(1) to create, O(n) to iterate (n = number of items)

## Description

The `enumerate()` function takes any iterable and returns an iterator that produces pairs containing an index (by default starting at 0) and the value from the iterable. It’s the most Pythonic way to get both index and item while looping, and avoids the anti-pattern of using `range(len(sequence))`.

## Usable With

Use `enumerate()` whenever you need both the index and the value from an iterable in a loop. Works with any iterable: lists, tuples, strings, sets, and custom iterators.

## Syntax

```python
enumerate(iterable, start=0)
```

- **explanation:**
  - `iterable` (required): any object capable of returning its members one at a time.
  - `start` (optional): the starting index (default is 0).

## Arguments

- **Required:** 1 (`iterable`)

- **Optional:** 1 (`start`, int)

- **Maximum:** 2

- **Required:**

```python
fruits = ["apple", "banana", "cherry"]
for idx, fruit in enumerate(fruits):
    print(idx, fruit)
# output:
# 0 apple
# 1 banana
# 2 cherry
```

- **Optional:**

```python
for idx, char in enumerate("abc", start=1):
    print(idx, char)
# output:
# 1 a
# 2 b
# 3 c
```

- **Maximum:**

```python
items = ["x", "y", "z"]
for i, item in enumerate(items, start=100):
    print(i, item)
# output:
# 100 x
# 101 y
# 102 z
```

## Examples

- **Enumerate over a list**

```python
colors = ["red", "green", "blue"]
for i, color in enumerate(colors):
    print(f"Color {i}: {color}")
# Output:
# Color 0: red
# Color 1: green
# Color 2: blue
```

- **Enumerate a string with custom start index**

```python
for i, letter in enumerate("dog", start=1):
    print(i, letter)
# Output:
# 1 d
# 2 o
# 3 g
```

- **Convert enumerate to a list of tuples**

```python
data = ["a", "b", "c"]
indexed = list(enumerate(data))
print(indexed)  # Output: [(0, 'a'), (1, 'b'), (2, 'c')]
```

**Note:** The object returned by `enumerate()` is an **iterator** and can be converted to a list or tuple if you need to access all pairs at once.

## Tips & Common mistakes

- Prefer `enumerate()` over `range(len(...))` for looping with index and value. It’s cleaner and less error-prone.
- The `start` parameter allows any integer (even negative or large numbers), which can be useful for custom indexing or offsets.
- The returned enumerate object is a generator/iterator, not a list—wrap with `list()` if you need all index-item pairs.
- Works with any iterable, not just sequences (e.g., file objects, generators).
- Unpack into two variables (`index, value`), but you can also use one for the tuple (`for pair in enumerate(...): ...`).
- If the underlying iterable changes length during the loop, results may be unexpected.

```python
# Enumerate with dictionary values
d = {"a": 1, "b": 2}
for idx, val in enumerate(d.values(), start=10):
    print(idx, val)
# output:
# 10 1
# 11 2
```

## See Also

- [`zip()`](zip)
- [`range()`](range)
- [`list()`](list)
- [`for`](for)
- [`enumerate() quiz generator` **R.W.E**](enumerate_rwe)
