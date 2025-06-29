---
id: strip
title: "strip()"
section: "String Methods"
tags: ["string", "method", "whitespace", "strip", "immutable", "both ends"]
see_also: ["lstrip()", "rstrip()", "replace()"]
works_with: ["str"]
---

# strip()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string)

## Description

The `strip()` method returns a new string with all leading (left) and trailing (right) whitespace removed. Optionally, you can specify a string of characters to remove instead of just whitespace. The original string is not changed (strings are immutable in Python).

## Usable With

Use `strip()` with any string. Very common for cleaning user input, data processing, and removing unwanted characters from both ends of a string.

## Syntax

```python
string.strip([chars])
```

- **explanation:** Call `strip()` on any string. The optional `chars` argument is a string specifying the set of characters to remove from both ends. If omitted, removes whitespace by default.

## Arguments

- **Required:** 0  
- **Optional:** 1 (`chars`, string: characters to remove from both ends)  
- **Maximum:** 1

```python
# Remove leading and trailing whitespace (default)
s = "   hello   "
print(s.strip())  # "hello"

# Remove specific characters from both ends
url = "...example.com..."
print(url.strip("."))  # "example.com"
```

## Examples

- **Trim whitespace from both ends**

```python
txt = "   Python   "
print(txt.strip())  # Output: "Python"
```

- **Remove multiple different leading and trailing characters**

```python
messy = "***###hello###***"
print(messy.strip("*#"))  # Output: "hello"
```

- **No effect if characters not present at ends**

```python
data = "data123"
print(data.strip("x"))  # Output: "data123" (unchanged)
```

**Note:** `strip()` only affects the *beginning* and *end* of the string, not characters in the middle.

## Tips & Common mistakes

- `strip()` does **not** modify the original string—always use or assign the return value.
- The `chars` argument removes **all** matching characters from both ends, not substrings and not from the middle.
- For removing only leading or trailing characters, use `lstrip()` or `rstrip()`.

```python
line = "---Hello---"
print(line.strip("-"))    # "Hello"
print(line.lstrip("-"))   # "Hello---"
print(line.rstrip("-"))   # "---Hello"
```

## See Also

- `lstrip()`
- `rstrip()`
- `replace()`
