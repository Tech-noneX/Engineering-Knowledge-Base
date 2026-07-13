---
id: print
title: "print()"
section: "Built-in Functions"
module: "built-in"
subscription: free
difficulty: beginner
reference: "Outputs values to the screen or another stream, separated by spaces"
tags: ['built-in', 'function', 'output', 'display', 'stream', 'console', 'print']
see_also: ['input()', 'str()', 'type()', 'format()', 'print() logging **R.W.E**']
works_with: ['str', 'int', 'float', 'list', 'tuple', 'dict', 'any object']
file path: 'docs\builtins\print_function.md'
---

# print()

- **Used with:** All Python objects (str, int, float, list, dict, etc.)
- **Construct:** function
- **Library:** Built-in
- **Iterable:** Yes (can print any iterable or unpacked arguments)
- **Time Complexity:** O(n) for n arguments (plus I/O)

## Description

The `print()` function displays one or more values to the console or standard output. By default, each item is separated by a space and the output ends with a newline. You can change the separator and ending, print to files, and unpack collections with `*`. Widely used for debugging, output, and user interaction.

## Usable With

Use `print()` for any type you want to display: strings, numbers, lists, dictionaries, or custom objects. Can print multiple items, unpack iterables, and redirect output to files.

## Syntax

```python
print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
```

- **explanation:**
  - `*objects`: One or more objects to print (separated by commas)
  - `sep`: String inserted between objects (default: space)
  - `end`: String printed at end (default: newline)
  - `file`: Output stream (default: console)
  - `flush`: Whether to forcibly flush the stream (default: False)

## Arguments

- **Required:** 0 (can be empty: `print()`)

- **Optional:** Unlimited (`*objects`, `sep`, `end`, `file`, `flush`)

- **Maximum:** Unlimited objects + 4 keyword-only args

- Required:

```python
print("Hello, world!")   # Prints: Hello, world!
print()                  # Prints a blank line
```

- Optional:

```python
print("A", "B", sep="-")                 # A-B
print("No newline", end="...")           # No newline...
print(1, 2, 3, sep=", ", end=" END\n")   # 1, 2, 3 END
```

- Maximum:

```python
import sys
print("Error!", file=sys.stderr, flush=True)
```

## Examples

- **Basic output**

```python
print("Welcome to Python!")  # Output: Welcome to Python!
```

- **Print multiple objects**

```python
x, y = 5, 7
print("x =", x, "y =", y)  # Output: x = 5 y = 7
```

- **Custom separator and end**

```python
print("A", "B", "C", sep="-", end="!?!\n")  # Output: A-B-C!?!
```

**Note:**  
You can print nothing (`print()`) for a blank line.  
Non-string objects are automatically converted with `str()`.

## Tips & Common mistakes

- `print()` can take any number of arguments of any type.
- Use `sep=""` for no spaces; use `end=""` to avoid a newline.
- Redirect output by setting `file` to a writable stream or file object.
- For debugging, use `print(repr(obj))` to see the raw value.
- Printing large data or in a loop may slow your program due to I/O.
- `print()` returns `None`, not the string—can’t assign result.

```python
with open("output.txt", "w") as f:
    print("Save this to file", file=f)
```

## See Also

- [`input()`](input)
- [`str()`](str)
- [`type()`](type)
- [`format()`](format)
- [`print() logging` **R.W.E**](print_rwe)
