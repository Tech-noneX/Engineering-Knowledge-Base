---
id: title
title: "title()"
section: "String Methods"
module: "built-in"
difficulty: beginner
subscription: premium
reference: "Returns a new string with the first letter of each word capitalized (title case)"
tags: ["string", "method", "case", "capitalize", "titlecase", "immutable"]
see_also: ["capitalize()", "lower()", "upper()", "title() format book titles **R.W.E**"]
works_with: ["str"]
---

# title()

- **Used with:** `str` (string)
- **Construct:** method
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(n) (n = length of the string)

## Description

The `title()` method returns a new string where the first character of each word is uppercase (capitalized) and all other characters are lowercase. Words are identified as sequences of characters separated by whitespace or non-letter characters. The original string is not modified (strings are immutable in Python).

## Usable With

Use `title()` with any string, typically for formatting names, titles, or user-facing text where each word should be capitalized.

## Syntax

```python
string.title()
```

- **explanation:** Call `title()` on any string to get a title-cased version.

## Arguments

- **Required:** 0  
- **Optional:** 0  
- **Maximum:** 0  

This method does **not** accept any arguments.

```python
# Correct usage
book = "war and peace"
print(book.title())   # Output: "War And Peace"
```

## Examples

- **Capitalize each word in a simple string**

```python
movie = "the godfather"
print(movie.title())  # Output: "The Godfather"
```

- **Handle strings with numbers and punctuation**

```python
s = "welcome to python 101: basics!"
print(s.title())  # Output: "Welcome To Python 101: Basics!"
```

- **Note special cases with apostrophes and acronyms**

```python
band = "ac/dc's greatest hits"
print(band.title())  # Output: "Ac/Dc'S Greatest Hits"
```

**Note:** `title()` may not handle apostrophes, contractions, or acronyms as humans would expect (e.g., "don't" → "Don'T", "McDonald" → "Mcdonald").

## Tips & Common mistakes

- `title()` does **not** modify the original string—always use or assign the return value.
- Not ideal for names with special capitalization ("O'Neil", "McDonald") or acronyms ("USA" → "Usa").
- For more advanced title casing (handling exceptions), consider using the third-party library `string.capwords()` or external packages like `titlecase`.

```python
phrase = "python is fun"
print(phrase.title())    # "Python Is Fun"
print(phrase)            # "python is fun"
```

## See Also

- `capitalize()`
- `lower()`
- `upper()`
- `title() format book titles` **R.W.E**
