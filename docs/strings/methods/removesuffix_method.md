---
id: removesuffix
title: "removesuffix()"
section: "String Methods"
module: "built-in"
difficulty: beginner
subscription: premium
reference: "Returns a new string with the specified suffix removed, if present"
tags: ["string", "method", "suffix", "remove", "immutable", "python3.9+"]
see_also: ["removeprefix()", "replace()", "strip()", "removesuffix() trim file extension **R.W.E**"]
works_with: ["str"]
file path: docs\strings\methods\removesuffix_method.md
---

# removesuffix()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in (Python 3.9+)
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string and suffix)

## Description

The `removesuffix()` method returns a new string with the specified suffix removed, if present. If the string ends with the given suffix, that part is removed; otherwise, the original string is returned unchanged. The original string is not modified (strings are immutable in Python).

## Usable With

Use `removesuffix()` on any string. Useful for trimming file extensions, cleaning up user input, or processing data with known fixed suffixes.

## Syntax

```python
string.removesuffix(suffix)
```

- **explanation:** Call `removesuffix()` on a string, passing the suffix you want to remove. Returns a new string.

## Arguments

- **Required:** 1 (`suffix`, string: the substring to remove from the end if present)
- **Optional:** 0
- **Maximum:** 1

```python
# Remove suffix if it matches
filename = "report.pdf"
print(filename.removesuffix(".pdf"))  # "report"

# No effect if suffix doesn't match
doc = "letter.doc"
print(doc.removesuffix(".pdf"))  # "letter.doc"
```

## Examples

- **Remove a matching suffix**

```python
url = "example.com/"
print(url.removesuffix("/"))  # Output: "example.com"
```

- **Suffix must be at the very end**

```python
path = "/user/data/"
print(path.removesuffix("data/"))  # Output: "/user/data/"
```

- **No effect if suffix not present**

```python
word = "banana"
print(word.removesuffix("apple"))  # Output: "banana"
```

**Note:** If the suffix is not present at the end, the original string is returned unchanged.

## Tips & Common mistakes

- `removesuffix()` does **not** modify the original string—always use or assign the return value.
- The method only removes the **exact** suffix at the end of the string (case-sensitive).
- Available in Python 3.9 and later. For older Python versions, use slicing or `str.endswith()` as a workaround.

```python
# Python < 3.9 workaround
s = "file.txt"
suffix = ".txt"
if s.endswith(suffix):
    s = s[:-len(suffix)]
print(s)  # "file"
```

## See Also

- [`removeprefix()`](removeprefix)
- [`replace()`](replace)
- [`strip()`](strip)
- [`if`](if)
- [`removesuffix() trim file extension` **R.W.E**](removesuffix_rwe)
