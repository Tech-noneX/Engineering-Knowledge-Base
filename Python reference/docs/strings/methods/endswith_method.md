---
id: endswith
title: endswith()
section: String Methods
module: str
subscription: premium
difficulty: beginner
reference: Checks if a string ends with a specified suffix; returns True or False.
tags: ['method', 'string', 'endswith', 'check', 'boolean']
see_also: ['startswith', 'find', 'index', 'lower']
works_with: ['str']
file_path: docs/strings/methods/endswith_method.md
---

# endswith()

- **Used with:** strings (`str`)
- **Construct:** `str.endswith(suffix[, start[, end]])`
- **Library:** Built-in
- **Iterable:** No (works on single strings)
- **Time Complexity:** O(N) (N = length of the checked portion)

## Description

The `endswith()` string method checks if the string **ends with** the specified suffix.  
It returns `True` if the string ends with the suffix, and `False` otherwise.

You can also specify optional `start` and `end` indexes to limit the check to a substring.

- **Safe to use:** Never raises an error—always returns a boolean.
- **Common use:** Input validation, file extension checking, pattern matching.

## Usable With

- Works on all `str` (string) objects.
- Suffix can be a string **or a tuple of strings** (for multiple possible endings).

## Syntax

```python
str.endswith(suffix[, start[, end]])
```

- `suffix`: String or tuple of strings to check for.
- `start` (optional): Index where to start searching.
- `end` (optional): Index where to stop searching.

## Arguments

- **Required:**  
  - `suffix`: The string (or tuple of strings) to check at the end of the string.

```python
'hello.py'.endswith('.py')      # True
```

- **Optional:**  
  - `start`: (int) Start index of the substring to check.
  - `end`: (int) End index of the substring to check.

```python
'archive.tar.gz'.endswith('.tar', 0, 11)    # True (checks only 'archive.tar')
```

- **Maximum:**  
  - `suffix` can be a tuple for multiple options.

```python
'main.py'.endswith(('.py', '.txt'))   # True (matches either suffix)
```

## Examples

- **Basic check:**  
  Check if a filename ends with `.txt`:

```python
filename = 'notes.txt'
filename.endswith('.txt')   # True
```

- **Check multiple possible endings:**  
  Useful for checking file extensions:

```python
file = 'photo.jpeg'
file.endswith(('.jpg', '.jpeg', '.png'))   # True
```

- **Check within a substring:**  
  Only look at part of the string:

```python
url = 'https://example.com/index.html'
url.endswith('.html', 0, 27)   # True
```

**Note:**  

- Case-sensitive—`.TXT` is different from `.txt`.
- Returns `False` if suffix is longer than the checked substring.

## Tips & Common mistakes

- **Case sensitivity:**  
  `'MyFile.TXT'.endswith('.txt')` is `False`. Use `.lower()` for case-insensitive checks:
  
  ```python
  'MyFile.TXT'.lower().endswith('.txt')  # True
  ```

- **Tuple for multiple options:**  
  Don't forget you can pass a tuple:
  
  ```python
  ext = ('.jpg', '.png')
  filename.endswith(ext)
  ```

- **Empty suffix always matches:**  
  `''.endswith('')` and `'abc'.endswith('')` both return `True`.

- **Index boundaries:**  
  If you specify a `start` and `end` that cut off the suffix, result will be `False`.

## See Also

- [`startswith()`](startswith)
- [`find()`](find)
- [`index()`](index)
- [`lower()`](lower)
