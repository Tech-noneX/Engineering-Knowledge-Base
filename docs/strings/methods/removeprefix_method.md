---
id: removeprefix
title: "removeprefix()"
section: "String Methods"
module: "built-in"
difficulty: beginner
subscription: premium
reference: "Returns a new string with the specified prefix removed, if present"
tags: ["string", "method", "prefix", "remove", "immutable", "python3.9+"]
see_also: ["removesuffix()", "replace()", "strip()", "removeprefix() clean log output **R.W.E**"]
works_with: ["str"]
---

# removeprefix()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in (Python 3.9+)
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string and prefix)

## Description

The `removeprefix()` method returns a new string with the specified prefix removed, if present. If the string starts with the given prefix, that part is removed; otherwise, the original string is returned unchanged. The original string is not modified (strings are immutable in Python).

## Usable With

Use `removeprefix()` on any string. Great for cleaning up input, file paths, URLs, log formatting, or processing data with known fixed prefixes.

## Syntax

```python
string.removeprefix(prefix)
```

- **explanation:** Call `removeprefix()` on a string, passing the prefix you want to remove. Returns a new string.

## Arguments

- **Required:** 1 (`prefix`, string: the substring to remove from the start if present)
- **Optional:** 0
- **Maximum:** 1

```python
# Remove prefix if it matches
s = "Python3.9"
print(s.removeprefix("Python"))  # "3.9"

# No effect if prefix doesn't match
s2 = "Java3.9"
print(s2.removeprefix("Python"))  # "Java3.9"
```

## Examples

- **Remove a matching prefix**

```python
filename = "test_log.txt"
print(filename.removeprefix("test_"))  # Output: "log.txt"
```

- **Prefix must be at the very start**

```python
url = "www.example.com"
print(url.removeprefix("http://"))  # Output: "www.example.com"
```

- **No effect if prefix not present**

```python
word = "banana"
print(word.removeprefix("apple"))  # Output: "banana"
```

**Note:** If the prefix is not present at the start, the original string is returned unchanged.

## Tips & Common mistakes

- `removeprefix()` does **not** modify the original string—always use or assign the return value.
- The method only removes the **exact** prefix at the start of the string (case-sensitive).
- Available in Python 3.9 and later. For older Python versions, use slicing or `str.startswith()` as a workaround.

```python
# Python < 3.9 workaround
s = "unittest"
prefix = "unit"
if s.startswith(prefix):
    s = s[len(prefix):]
print(s)  # "test"
```

## See Also

- `removesuffix()`
- `replace()`
- `strip()`
- `removeprefix() clean log output` **R.W.E**
