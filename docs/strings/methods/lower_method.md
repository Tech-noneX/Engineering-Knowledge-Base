---
id: lower
title: "lower()"
section: "String Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Returns a copy of the string with all letters converted to lowercase"
tags: ["string", "method", "case", "text", "immutable"]
see_also: ["upper()", "capitalize()", "casefold()", "if", lower() normalize user input **R.W.E**"]
works_with: ["str"]
file path: 'docs\strings\methods\lower_method.md'
---

# lower()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string)

## Description

The `lower()` method returns a copy of the string with all uppercase characters converted to lowercase. It does **not** change the original string - strings in Python are immutable. Non-alphabetical characters and lowercase letters remain unchanged.

## Usable With

Use `lower()` with any string. Commonly used for normalizing text, case-insensitive comparisons, searching, or preparing data for consistent processing.

## Syntax

```python
string.lower()
```

- **explanation:** Call `lower()` on any string variable. Returns a new string in all lowercase.

## Arguments

- **Required:** 0
- **Optional:** 0
- **Maximum:** 0

This method takes **no arguments**.

```python
# Correct usage
text = "Hello World"
lower_text = text.lower()  # 'hello world'
```

## Examples

- **Convert a mixed-case string to all lowercase**

```python
greeting = "Good Morning!"
print(greeting.lower())   # Output: "good morning!"
```

- **Normalize user input for comparison**

```python
user_input = "YES"
if user_input.lower() == "yes":
    print("User said yes!")  # Output: User said yes!
```

- **Using with non-alphabetic characters**

```python
special = "1234 ABC xyz!"
print(special.lower())  # Output: "1234 abc xyz!"
```

**Note:** `lower()` does not modify the original string.

## Tips & Common mistakes

- `lower()` does **not** change the original string—always use the return value or assign it to a variable.
- Only affects uppercase letters (A-Z). Other characters are not changed.
- For more aggressive case folding (e.g., for some non-English characters), use `casefold()` instead of `lower()`.

```python
word = "HELLO"
word.lower()      # Correct: returns "hello", but word is still "HELLO"
print(word)       # "HELLO"

word = word.lower()  # Now word is "hello"
print(word)          # "hello"
```

## See Also

- [`upper()`](upper)
- [`capitalize()`](capitalize)
- [`casefold()`](casefold)
- [`if`](if)
- [`lower() normalize user input` **R.W.E**](lower_rwe)
