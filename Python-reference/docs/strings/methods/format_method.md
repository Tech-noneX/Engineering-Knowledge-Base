---
id: format
title: format()
section: String Methods
module: built-in
subscription: free
difficulty: beginner
reference: Format strings with placeholders and variable values
tags: ['string', 'method', 'format', 'interpolation', 'replace', 'template']
see_also: ['f-string', 'replace', 'join', 'str']
works_with: ['str']
file_path: Python-reference/docs/strings/methods/format_method.md
---

# format()

- **Used with:** strings (as a method)
- **Construct:** method (called on a string)
- **Library:** built-in
- **Iterable:** works with any number of arguments (not itself iterable)
- **Time Complexity:** O(n) where n is the length of the result string and number of replacements

## Description

The `format()` string method inserts values into a string using curly-brace `{}` placeholders.  
It’s the classic way to combine text and variables for output, logs, reports, and dynamic messages—especially before f-strings (Python 3.6+).

## Usable With

Use with any string that includes curly-brace placeholders.  
Accepts variables, literals, expressions, and can work with both positional and named arguments.

## Syntax

```python
"template string with {}".format(value)
```

- **explanation:**  
  Call `.format()` on a string containing `{}` placeholders.  
  Each placeholder is replaced by the corresponding argument to `.format()` in order (positional or named).

## Arguments

- **Required:** 0 (can call with no arguments if no placeholders)

- **Optional:** Unlimited (`*args`, `**kwargs` — any values you want to insert)

- **Maximum:** As many as there are placeholders

- Required:

```python
"Hello, {}".format("world")
# Replaces the {} with "world"
```

- Optional:

```python
"{greeting}, {name}!".format(greeting="Hi", name="Alice")
# Uses named placeholders for flexibility
```

- Maximum

```python
"{} + {} = {}".format(2, 3, 2+3)
# Fills multiple placeholders in order
```

## Examples

- **Format with positional arguments**  
  Combine variables in order into a readable sentence.

```python
animal = "dog"
count = 3
print("I have {} {}s.".format(count, animal))
# Output: I have 3 dogs.
```

- **Format with named arguments**  
  Fill placeholders by variable name for clarity.

```python
msg = "User: {user} | Score: {score}"
print(msg.format(user="Mia", score=88))
# Output: User: Mia | Score: 88
```

- **Use formatting options (decimals, alignment, padding)**  
  Control the appearance of numbers or text.

```python
price = 5.678
print("Price: ${:.2f}".format(price))
# Output: Price: $5.68
```

- **Fill placeholders with values from a dictionary using ** unpacking**
  This is useful when your variable names and dictionary keys match.

```python
data = {'name': 'Bob', 'score': 42}
print("User: {name}, Score: {score}".format(**data))
# Output: User: Bob, Score: 42
```

**Note:**  
`format()` does not modify the original string—it always returns a new string.  
Unmatched or missing placeholders will raise an error.

## Tips & Common mistakes

- Placeholders `{}` must match the number of arguments—or use named arguments to avoid confusion.
- For advanced formatting (like alignment or decimal places), use a colon: `{:.2f}` for two decimals, `{:>10}` for right-align.
- f-strings (Python 3.6+) are faster and more readable for most new code, but `format()` is still useful for older code or complex formatting.

```python
# Common mistake: mismatched placeholders and arguments
"{} {} {}".format(1, 2)
# IndexError: tuple index out of range

# Tip: Use double curly braces to show a literal '{' or '}'
print("Use {{}} to escape curly braces.".format())
# Output: Use {} to escape curly braces.
```

## See Also

- [`f-string`](f-string)
- [`replace`](replace)
- [`join`](join)
- [`str`](str)
