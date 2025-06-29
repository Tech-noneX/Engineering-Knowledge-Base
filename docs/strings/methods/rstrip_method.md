---
id: rstrip
title: "rstrip()"
section: "String Methods"
tags: ["string", "method", "whitespace", "strip", "immutable", "right"]
see_also: ["lstrip()", "strip()", "replace()"]
works_with: ["str"]
---

# rstrip()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string)

## Description

The `rstrip()` method returns a new string with all trailing (right-side) whitespace removed. Optionally, you can specify a string of characters to remove instead of just whitespace. The original string is not changed (strings are immutable in Python).

## Usable With

Use `rstrip()` with any string. Often used for cleaning up user input, data processing, or removing unwanted characters from the end of strings.

## Syntax

```python
string.rstrip([chars])
```

- **explanation:** Call `rstrip()` on any string. The optional `chars` argument is a string specifying the set of characters to remove from the right. If omitted, removes whitespace by default.

## Arguments

- **Required:** 0  
- **Optional:** 1 (`chars`, string: characters to remove from the end)  
- **Maximum:** 1

```python
# Remove trailing whitespace (default)
s = "hello   "
print(s.rstrip())  # "hello"

# Remove specific trailing characters
data = "123abc!!!"
print(data.rstrip("!c"))  # "123ab"
```

## Examples

- **Trim right-side whitespace**

```python
msg = "Python   "
print(msg.rstrip())  # Output: "Python"
```

- **Remove multiple different trailing characters**

```python
fancy = "***###hello###***"
print(fancy.rstrip("*#"))  # Output: "***###hello"
```

- **No effect if trailing characters not in 'chars'**

```python
data = "data123"
print(data.rstrip("x"))  # Output: "data123" (unchanged)
```

**Note:** `rstrip()` only affects the *end* of the string.

## Tips & Common mistakes

- `rstrip()` does **not** modify the original string—always use or assign the return value.
- If you provide a string to `chars`, **every** character in that string will be removed from the end until a character not in `chars` is found (it is not treated as a substring).
- To remove whitespace from both ends, use `strip()`. To remove from the left, use `lstrip()`.

```python
line = "---Hello---"
print(line.rstrip("-"))   # "---Hello"
print(line.lstrip("-"))   # "Hello---"
print(line.strip("-"))    # "Hello"
```

## See Also

- `lstrip()`
- `strip()`
- `replace()`
