---
id: lstrip
title: "lstrip()"
section: "String Methods"
tags: ["string", "method", "whitespace", "strip", "immutable", "left"]
see_also: ["rstrip()", "strip()", "replace()"]
works_with: ["str"]
---

# lstrip()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string)

## Description

The `lstrip()` method returns a new string with all leading (left) whitespace removed. Optionally, you can specify a string of characters to remove instead of just whitespace. The original string is not modified (strings are immutable in Python).

## Usable With

Use `lstrip()` with any string. Common for cleaning user input, trimming spaces, or removing unwanted characters from the left side of a string.

## Syntax

```python
string.lstrip([chars])
```

- **explanation:** Call `lstrip()` on any string. The optional `chars` argument is a string specifying the set of characters to remove from the left. If omitted, removes whitespace by default.

## Arguments

- **Required:** 0  
- **Optional:** 1 (`chars`, string: characters to remove from the start)  
- **Maximum:** 1

```python
# Remove leading whitespace (default)
s = "   hello"
print(s.lstrip())  # "hello"

# Remove specific leading characters
url = "www.example.com"
print(url.lstrip("w."))  # "example.com"
```

## Examples

- **Trim left-side whitespace**

```python
txt = "   Python"
print(txt.lstrip())  # Output: "Python"
```

- **Remove multiple different leading characters**

```python
fancy = "***###hello###***"
print(fancy.lstrip("*#"))  # Output: "hello###***"
```

- **No effect if leading characters not in 'chars'**

```python
data = "123abc"
print(data.lstrip("x"))  # Output: "123abc" (unchanged)
```

**Note:** `lstrip()` only affects the *beginning* of the string.

## Tips & Common mistakes

- `lstrip()` does **not** change the original string—always use or assign the return value.
- If you pass a string to `chars`, **every** character in that string will be removed from the left until a character not in `chars` is found (it is not treated as a substring).
- To remove whitespace from both ends, use `strip()`. To remove from the right, use `rstrip()`.

```python
line = "---Hello---"
print(line.lstrip("-"))   # "Hello---"
print(line.rstrip("-"))   # "---Hello"
print(line.strip("-"))    # "Hello"
```

## See Also

- `rstrip()`
- `strip()`
- `replace()`
