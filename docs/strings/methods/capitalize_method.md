---
id: capitalize
title: "capitalize()"
section: "String Methods"
tags: ["string", "method", "case", "capitalize", "immutable", "sentence case"]
see_also: ["title()", "upper()", "lower()"]
works_with: ["str"]
---

# capitalize()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string)

## Description

The `capitalize()` method returns a copy of the string with the first character capitalized (uppercase) and the rest of the characters lowercased. Useful for formatting text in “sentence case.” The original string is not modified (strings are immutable in Python).

## Usable With

Use `capitalize()` on any string, especially for formatting user input, names, or displaying single-sentence text in a standard way.

## Syntax

```python
string.capitalize()
```

- **explanation:** Call `capitalize()` on any string. Returns a new string with only the first character capitalized.

## Arguments

- **Required:** 0  
- **Optional:** 0  
- **Maximum:** 0

This method takes **no arguments**.

```python
# Basic usage
s = "hello world"
print(s.capitalize())  # "Hello world"
```

## Examples

- **Capitalize the first character, lower the rest**

```python
msg = "pYTHON is AWESOME!"
print(msg.capitalize())  # Output: "Python is awesome!"
```

- **Works with strings starting with whitespace (only first letter after whitespace is affected)**

```python
data = "   hello"
print(data.capitalize())  # Output: "   hello"
```

- **Single letter string**

```python
letter = "x"
print(letter.capitalize())  # Output: "X"
```

**Note:** Only the very first character is capitalized. All others are lowercased, which may not be ideal for names or titles.

## Tips & Common mistakes

- `capitalize()` does **not** modify the original string—always use or assign the return value.
- Only the **first character** is capitalized, the rest are made lowercase. For title case (every word capitalized), use `title()`.
- Does not handle multi-word proper nouns correctly ("john DOE" → "John doe").
- Leading whitespace is preserved; only the first non-whitespace character is affected.

```python
name = "jOhN dOE"
print(name.capitalize())   # "John doe"
print(name.title())        # "John Doe"
```

## See Also

- `title()`
- `upper()`
- `lower()`
