---
id: find
title: 'find()'
section: 'String Methods'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Returns the lowest index of a substring, or -1 if not found'
tags: ['string', 'method', 'find', 'substring', 'index', 'search', 'text']
see_also: ['index()', 'count()', 'replace()', 'find() all positions **R.W.E**']
works_with: ['str']
file path: docs\strings\methods\find_method.md'
---

# find()

- **Used with:** str
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No (searches internally, returns integer)
- **Time Complexity:** O(n*m), where n = length of string, m = length of substring

## Description

The `find()` string method returns the **lowest index** in the string where a specified substring is found.  
Returns `-1` if the substring is not found.  
Safe for searching, as it never raises an error (unlike `index()`).

## Usable With

Strings only.  
Searches for a substring within another string.

## Syntax

```python
str.find(sub[ , start[ , end]])
```

- **explanation:**  
  - `sub`: The substring to search for (required).
  - `start`: The starting index to search from (optional).
  - `end`: The ending index to search to (optional).
  - Returns: The index of the first match, or `-1` if not found.

## Arguments

- **Required:** 1 (`sub`)

- **Optional:** 2 (`start`, `end`)

- **Maximum:** 3

- Required:

```python
text = "hello world"
i = text.find("world")  # returns 6
```

- Optional:

```python
msg = "banana"
pos = msg.find('a', 2)  # returns 3 (finds 'a' after index 2)
```

- Maximum

```python
data = "abracadabra"
result = data.find('a', 3, 7)  # returns 5
```

## Examples

- **Find the position of a substring**

```python
phrase = "cat and dog"
pos = phrase.find("dog")
print(pos) # pos is 8
```

- **Substring not found (returns -1)**

```python
line = "hello"
print(line.find("z"))  # prints -1
```

- **Search within a range**

```python
s = "abracadabra"
print(s.find("a", 2, 7))  # prints 5
```

**Note:**  
Returns the lowest index only; for all positions, use a loop or regular expressions.

## Tips & Common mistakes

- Use `find()` if you don’t want an error when the substring is missing (returns `-1`).
- For strict error handling, use `str.index()` (raises `ValueError` if not found).
- Start and end are slice indexes (like with string slicing).
- For all matches, use a loop or regex (`re.finditer`).

```python
s = "aaa"
positions = []
i = s.find("a")
while i != -1:
    positions.append(i)
    i = s.find("a", i + 1)
# positions is [0, 1, 2]
```

## See Also

- [`index()`](index)
- [`count()`](count)
- [`replace()`](replace)
- [`find() all positions` **R.W.E**](find_rwe)
