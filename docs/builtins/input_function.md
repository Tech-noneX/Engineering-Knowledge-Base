---
id: input
title: 'input()'
section: 'Built-in Functions'
module: 'built-in'
subscription: free
difficulty: beginner
reference: 'Gets a line of user input as a string from the console'
tags: ['built-in', 'function', 'input', 'user', 'string', 'console', 'prompt']
see_also: ['print()', 'str()', 'int()', 'type()', 'input() input validation **R.W.E**']
works_with: ['str', 'user', 'console']
---

# input()

- **Used with:** Console/user input (returns string)
- **Construct:** function
- **Library:** Built-in
- **Iterable:** No (returns a single string)
- **Time Complexity:** O(n), where n = length of input

## Description

The `input()` function pauses program execution, displays an optional prompt, and waits for the user to enter text, which is returned as a string. Common for collecting information or choices from the user in CLI apps. Always returns a string—convert to other types as needed (e.g., `int()`).

## Usable With

Use `input()` to read text entered by the user at the keyboard. The input is always a string, even if the user types a number.

## Syntax

```python
input([prompt])
```

- **explanation:**  
  - `prompt` (optional): String displayed to the user before input.  
  - Returns: The entered text as a string.

## Arguments

- **Required:** 0

- **Optional:** 1 (`prompt`, str)

- **Maximum:** 1

- Required:

```python
name = input()
```

- Optional:

```python
age = input("Enter your age: ")
```

- Maximum

```python
color = input("What is your favorite color? ")
```

## Examples

- **Basic input (no prompt)**

```python
text = input()
print("You entered:", text)
```

- **Input with a prompt**

```python
name = input("What is your name? ")
print("Hello,", name)
```

- **Convert input to another type**

```python
num = int(input("Enter a number: "))
print("Twice your number:", num * 2)
```

**Note:**  
`input()` always returns a string, even if the user enters numbers. Use `int()` or `float()` to convert as needed.

## Tips & Common mistakes

- `input()` always returns a **string**—convert to `int` or `float` if you need numbers.
- Don’t forget to add prompts so users know what to enter.
- Be ready for errors: if user input is not what you expect (e.g., letters instead of numbers), your program may crash—use `try/except` for safe conversion.

```python
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("That was not a valid number!")
```

## See Also

- [`print()`](print)
- [`str()`](str)
- [`int()`](int)
- [`type()`](type)
- [`input() input validation` **R.W.E**](input_rwe)
