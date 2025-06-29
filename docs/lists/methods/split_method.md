---
id: split
title: "split()"
section: "String Methods"
tags: ["string", "method", "split", "delimiter", "text", "conversion"]
see_also: ["join()", "partition()", "rsplit()"]
works_with: ["string"]
---

# split

- **Used with:**  
strings  
- **Construct:**  
Method  
- **Library:**  
Built-in  
- **Iterable:**  
Yes (returns a list)  
- **Time Complexity:**  
O(n) (where n is the length of the string)

## Description

Splits a string into a list of substrings based on a separator (delimiter).  
If no separator is specified, it splits on any whitespace by default.

## Usable With

Python `str` objects.

## Syntax

```python
str.split(sep=None, maxsplit=-1)
```

- **explanation:**
  - `str`: Your string variable (e.g., `"hello world"`).
  - `.split()`: Method called on the string.
  - `sep=None`: (Optional) String delimiter to split by. If not specified or `None`, splits on whitespace.
  - `maxsplit=-1`: (Optional) Maximum number of splits. `-1` means no limit.
  - Returns a **list** of substrings.

## Arguments

**Required:** 0 (both arguments are optional)  
**Optional:** 2 (`sep`, `maxsplit`)  
**Maximum:** 2

- Required:

```python
# No required arguments; can be used with none.
"hello world".split()  # ['hello', 'world']
```

- Optional:

```python
sep  # (Optional) The delimiter to split by.
# Example:
"one,two,three".split(',')  # ['one', 'two', 'three']

maxsplit  # (Optional) Maximum splits to do.
# Example:
"a b c d".split(' ', 2)  # ['a', 'b', 'c d']
```

- Maximum

```python
# Using both arguments:
"apple,banana,cherry".split(',', 1)  # ['apple', 'banana,cherry']
```

## Examples

- **Split a string by whitespace**

```python
sentence = "hello world"
words = sentence.split()
# words is ['hello', 'world']
```

- **Split by a specific delimiter**

```python
data = "apple,banana,cherry"
fruits = data.split(',')
# fruits is ['apple', 'banana', 'cherry']
```

- **Split with a maxsplit limit**

```python
text = "a b c d"
parts = text.split(' ', 2)
# parts is ['a', 'b', 'c d']
```

 **Note:**  

- If `sep` is not specified or is `None`, consecutive whitespace is treated as a single separator.
- If the string starts or ends with the separator, the result will include empty strings at the ends.

## Tips & Common mistakes

- Using `split()` with no argument splits on *any* whitespace (spaces, tabs, newlines).
- If the delimiter does not occur in the string, `split()` returns a list containing the original string.
- If `maxsplit=0`, no splitting occurs, returns the whole string in a single-element list.
- Works only on strings; use `re.split()` for regular expression splits.
- Trailing delimiters produce empty strings in the result.

```python
# Example with trailing delimiter:
"one,two,".split(',')  # ['one', 'two', '']
```
