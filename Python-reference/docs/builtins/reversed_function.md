---
id: reversed
title: "reversed()"
section: "Built-in Functions"
module: "built-in"
difficulty: beginner
subscription: free
reference: Returns an iterator that yields items in reverse order
tags: ["built-in", "function", "reverse", "sequence", "iteration", "for loop", "iterator"]
see_also: ["list()", "range()", "for", "sorted()", "reversed() undo navigation"]
works_with: ["list", "tuple", "str", "range", "sequence", "iterable"]
file_path: Python-reference/docs/builtins/reversed_function.md
---

# reversed()

- **Used with:** Sequences (lists, tuples, strings, ranges, etc.)
- **Construct:** function (returns a reverse iterator)
- **Library:** Built-in
- **Iterable:** Yes
- **Time Complexity:** O(1) to create the iterator, O(n) to iterate (n = number of elements)

## Description

The `reversed()` function returns a reverse iterator over the given sequence. It allows you to loop over items in reverse order without creating a new reversed copy of the sequence (memory efficient). For objects that support the sequence protocol (define `__len__()` and `__getitem__()`), such as lists, tuples, strings, and ranges.

## Usable With

Use `reversed()` with lists, tuples, strings, ranges, dictionaries, or custom
objects that implement `__reversed__()`. It also supports objects with the
sequence protocol (`__len__()` and integer-based `__getitem__()`). Sets must be
converted to an ordered sequence first because they do not define reverse order.

## Syntax

```python
reversed(sequence)
```

- **explanation:** Pass a sequence to `reversed()` to get an iterator that yields elements in reverse order.

## Arguments

- **Required:** 1 (`sequence`: a sequence object)
- **Optional:** 0
- **Maximum:** 1

```python
# Basic usage
nums = [1, 2, 3]
rev = reversed(nums)
print(list(rev))  # [3, 2, 1]
```

## Examples

- **Loop over a list in reverse**

```python
values = [10, 20, 30]
for v in reversed(values):
    print(v)
# Output: 30 20 10
```

- **Reverse a string**

```python
text = "Python"
print("".join(reversed(text)))  # Output: "nohtyP"
```

- **Reverse a range**

```python
for i in reversed(range(3)):
    print(i)
# Output: 2 1 0
```

- **Reverse dictionary keys (Python 3.8+)**

```python
settings = {"voltage": 230, "current": 5, "phase": 1}
print(list(reversed(settings)))
# ['phase', 'current', 'voltage']
```

**Note:** For objects that don’t support `__len__()` and `__getitem__()`, use `list(reversed(obj))` or `reversed(list(obj))`.

## Tips & Common mistakes

- `reversed()` returns an **iterator**—to get a list, use `list(reversed(sequence))`.
- Does **not** work directly with sets because a set has no defined order.
- Dictionaries are reversible in Python 3.8+ and yield keys in reverse insertion order.
- Custom objects can support it through `__reversed__()` or the sequence protocol.
- If you need to reverse in place (for lists), use the `.reverse()` method instead.

```python
# Reverse a tuple as a list
tup = (1, 2, 3)
print(list(reversed(tup)))  # [3, 2, 1]
```

## See Also

- [`list()`](list)
- [`range()`](range)
- [`for`](for)
- [`sorted()`](sorted)
- [`reversed() undo navigation` **R.W.E**](reversed_rwe)
