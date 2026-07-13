---
id: partition
title: partition()
section: String Methods
module: built-in
subscription: premium
difficulty: beginner
reference: 'Splits a string into a 3-tuple at the first occurrence of a separator.'
tags: ['string', 'method', 'partition', 'split', 'separator', 'tuple']
see_also: ['split()', 'rsplit()', 'find()', 'replace()', 'rpartition()']
works_with: ['str']
file path: 'docs\strings\methods\partition_method.md'
---

# partition()

- **Used with:** String objects (`str`)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (returns a tuple)
- **Time Complexity:** O(n), where n = length of the string

## Description

The `partition()` method splits a string into a 3-tuple using the **first occurrence** of the specified separator. The result is always a tuple of three elements:

1. The part before the separator
2. The separator itself
3. The part after the separator

If the separator is not found, returns a tuple containing the original string and two empty strings. 

Commonly used for extracting data before/after a character or substring, such as splitting on `:` in config files or CSVs.

## Usable With

- Works only with strings (`str`).
- Use for parsing, extracting, or splitting data based on the first occurrence of a substring.

## Syntax

```python
str.partition(sep)
```

- **explanation:**
  - `sep` (required): The separator to search for (string).
  - Returns a tuple of (part_before, separator, part_after).

## Arguments

- **Required:** 1 (`sep`)
- **Optional:** 0
- **Maximum:** 1

- Required:

```python
sentence = "a:b:c"
parts = sentence.partition(":")
# parts is ('a', ':', 'b:c')
```

- Optional:

```python
# No optional arguments; only the separator is required.
```

- Maximum

```python
# Only one argument allowed (the separator)
```

## Examples

- **Partition with a space separator**

```python
text = "hello world python"
result = text.partition(" ")
print(result)  
# Output: ('hello', ' ', 'world python')
```

- **Separator not found**

```python
value = "banana"
print(value.partition(","))  
# Output: ('banana', '', '')
```

- **Partition on first occurrence only**

```python
s = "id:42:active"
print(s.partition(":"))  
# Output: ('id', ':', '42:active')
```

**Note:** `partition()` always returns a 3-tuple. It only splits at the **first** occurrence, not all.

## Tips & Common mistakes

- Always returns a 3-tuple, even if the separator is not found.
- Only splits at the first occurrence. For all splits, use `split()`.
- If you need to split from the right, use `rsplit()` or `rpartition()`.
- If the separator is not found, the original string is returned as the first item, with two empty strings as the other elements.

```python
info = "data"
print(info.partition(":"))  # ('data', '', '')
```

## See Also

- [`split()`](split)
- [`rsplit()`](rsplit)
- [`find()`](find)
- [`replace()`](replace)
- [`rpartition()`](rpartition)
