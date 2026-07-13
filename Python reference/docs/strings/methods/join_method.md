---
id: join
title: 'join()'
section: 'String Methods'
module: 'built-in'
subscription: premium
difficulty: beginner
reference: 'Concatenates items of an iterable into a single string with a separator'
tags: ['string', 'method', 'join', 'concatenate', 'separator', 'combine', 'text']
see_also: ['split()', 'replace()', 'format()', 'comprehension', 'join() CSV row **R.W.E**']
works_with: ['str', 'list', 'tuple', 'iterable']
file path: 'docs\strings\methods\join_method.md'
---

# join()

- **Used with:** str (as the separator), plus any iterable of strings (list, tuple, etc.)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** Yes (works with any iterable of strings)
- **Time Complexity:** O(n), where n = total length of the final string

## Description

The `join()` string method combines the elements of an iterable (such as a list or tuple of strings) into a single string, with the original string used as the separator.  
Efficient for creating CSV lines, paths, or combining words and values.

## Usable With

Call on a string (used as the separator), passing any iterable of strings (e.g., list, tuple).  
All items in the iterable must be strings—use `str()` to convert other types.

## Syntax

```python
separator.join(iterable)
```

- **explanation:**  
  - `separator`: The string to place between elements (e.g., ', ', '-', '').  
  - `iterable`: An iterable of strings to join together.
  - Returns: The concatenated string.

## Arguments

- **Required:** 1 (`iterable` of strings)
- **Optional:** 0
- **Maximum:** 1

- Required:

```python
words = ['Python', 'is', 'fun']
result = ' '.join(words)  # 'Python is fun'
```

- Optional:

```python
# No optional arguments; only the iterable is required
```

- Maximum

```python
# Only one argument allowed (the iterable)
```

## Examples

- **Join words with a space**

```python
words = ['AI', 'Python', 'Pocket']
sentence = ' '.join(words)
# sentence is 'AI Python Pocket'
```

- **Join with commas (CSV)**

```python
fields = ['name', 'age', 'city']
csv_line = ','.join(fields)
# csv_line is 'name,age,city'
```

- **Join with no separator**

```python
letters = ['a', 'b', 'c']
joined = ''.join(letters)
# joined is 'abc'
```

**Note:**  
All items in the iterable **must be strings**. If not, use `str()` to convert them.

## Tips & Common mistakes

- Remember to call `join()` **on the separator**, not the iterable (e.g., `', '.join(list)`).
- All items must be strings—use a generator or list comprehension for conversion:  
  `', '.join(str(x) for x in items)`
- Much more efficient than repeated `+` string concatenation, especially in loops.
- Returns a new string; original data is unchanged.

```python
nums = [1, 2, 3]
result = ', '.join(str(n) for n in nums)
# result is '1, 2, 3'
```

## See Also

- [`split()`](split)
- [`replace()`](replace)
- [`format()`](format)
- [`comprehension`](comprehension)
- [`join() CSV row` **R.W.E**](join_rwe)
