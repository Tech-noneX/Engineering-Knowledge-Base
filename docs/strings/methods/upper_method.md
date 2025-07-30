---
id: upper
title: "upper()"
section: "String Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Returns a copy of the string with all letters converted to uppercase"
tags: ["string", "method", "case", "uppercase", "text"]
see_also: ["lower()", "capitalize()", "title()", "casefold()", "upper() normalize codes **R.W.E**"]
works_with: ["str"]
file path: docs\strings\methods\upper_method.md
---

# upper()

- **Used with:** `str` (string)
- **Construct:**  method
- **Library:**  Built-in
- **Iterable:**  Not iterable (acts on a single string)
- **Time Complexity:** O(n), where n is the length of the string

## Description

Converts all lowercase letters in a string to uppercase and returns a **new string**. Non-alphabetic characters and already-uppercase letters remain unchanged. This method does **not** modify the original string (strings are immutable in Python).

## Usable With

Works with any string (`str`). Useful for formatting output, case-insensitive comparisons, processing user input, and data normalization.

## Syntax

```python
string.upper()
```

- **explanation:**  
  Call `upper()` on any string object. Returns a new string with all alphabetic characters converted to uppercase.

## Arguments

- **Required:** None  
- **Optional:** None  
- **Maximum:** None

No arguments are passed to `upper()`.

```python
# No arguments required
my_text.upper()
```

## Examples

- **Basic usage**

```python
name = "hello world"
print(name.upper())  # Output: "HELLO WORLD"
```

*Converts all letters to uppercase.*

- **With mixed case and symbols**

```python
info = "Python 3.10 rocks!"
result = info.upper()
print(result)  # Output: "PYTHON 3.10 ROCKS!"
```

*Numbers and symbols are unchanged; only letters are affected.*

- **Case-insensitive comparison**

```python
user_input = "Yes"
if user_input.upper() == "YES":
    print("Confirmed!")
```

*Makes string comparison case-insensitive.*

**Note:**  
The original string is not modified. A new uppercase string is returned.

## Tips & Common mistakes

- **Tip:** `upper()` does **not** change the original string; it returns a new string.
- **Tip:** Use `upper()` (or `lower()`) for case-insensitive comparisons.
- **Common mistake:** Trying to pass arguments to `upper()` (`str.upper(some_arg)`) will cause an error- it takes **no arguments**.
- **Common mistake:** Expecting non-letter characters (like numbers or punctuation) to be changed-  **they are not affected**.

```python
# Common mistake
text = "hello"
text.upper("wrong")  # TypeError: upper() takes no arguments
```

## See Also

- [`lower()`](lower)
- [`capitalize()`](capitalize)
- [`title()`](title)
- [`casefold()`](casefold)
- [`upper() normalize codes` **R.W.E**](upper_rwe)
