---
id: replace
title: "replace()"
section: "String Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Returns a new string with all (or a limited number of) occurrences of a substring replaced"
tags: ["string", "method", "replace", "immutable", "substring", "count"]
see_also: ["removeprefix()", "removesuffix()", "strip()", "replace() clean CSV values **R.W.E**"]
works_with: ["str"]
file path: docs\strings\methods\replace_method.md
---

# replace()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n * m) (n = length of the string, m = number of replacements)

## Description

The `replace()` method returns a new string with all occurrences of a specified substring replaced by another substring. You can optionally specify the maximum number of replacements to perform. The original string is not modified (strings are immutable in Python).

## Usable With

Use `replace()` on any string. Common for cleaning data, normalizing text, replacing words, characters, formatting, or correcting typos.

## Syntax

```python
string.replace(old, new[, count])
```

- **explanation:** Call `replace()` on a string, passing:
  - `old` (required): the substring to replace,
  - `new` (required): the replacement substring,
  - `count` (optional): the maximum number of occurrences to replace (defaults to all).

## Arguments

- **Required:** 2 (`old`, `new`)
- **Optional:** 1 (`count`, int: maximum replacements)
- **Maximum:** 3

```python
# Replace all
text = "hello world"
print(text.replace("l", "x"))  # "hexxo worxd"

# Replace up to 1
s = "one one one"
print(s.replace("one", "two", 1))  # "two one one"
```

## Examples

- **Replace all occurrences of a substring**

```python
email = "foo@foo.com"
print(email.replace("foo", "bar"))  # Output: "bar@bar.com"
```

- **Replace with a limited count**

```python
text = "abc abc abc"
print(text.replace("abc", "xyz", 2))  # Output: "xyz xyz abc"
```

- **No effect if substring not found**

```python
greeting = "hello"
print(greeting.replace("bye", "hi"))  # Output: "hello"
```

**Note:** Replacement is case-sensitive. If `old` is not found, the original string is returned unchanged.

## Tips & Common mistakes

- `replace()` does **not** modify the original string—always use or assign the return value.
- Replacement is **case-sensitive**: `"A".replace("a", "b")` returns `"A"`.
- To remove a substring, use `replace(substring, "")`.
- For multiple different replacements, chain `replace()` calls or use regular expressions for more advanced patterns.

```python
# Remove all spaces
s = "hello world"
print(s.replace(" ", ""))  # "helloworld"
```

## See Also

- [`removeprefix()`](removepreffix)
- [`removesuffix()`](removesuffix)
- [`strip()`](strip)
- [`replace() clean CSV values` **R.W.E**](replace_rwe)
