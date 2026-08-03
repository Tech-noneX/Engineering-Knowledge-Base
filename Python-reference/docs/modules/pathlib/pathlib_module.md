---
id: pathlib
title: 'pathlib'
section: 'Modules'
module: 'standard library'
subscription: free
difficulty: beginner
reference: 'Object-oriented paths for reading, creating, writing and appending files'
tags: ['file', 'path', 'pathlib', 'read', 'write', 'append', 'text', 'data']
see_also: ['str()', 'split()', 'join()', 'int()']
works_with: ['Path', 'str', 'list']
file_path: Python-reference/docs/modules/pathlib/pathlib_module.md
---

## pathlib

- **Category:** Standard Library
- **Installation & Import:** Included with Python; no `pip` installation is required
- **Common Use Cases:** Constructing paths and reading, creating, writing and appending files
- **Key Class:** `Path`
- **Key Methods and Properties:** `resolve()`, `parent`, `read_text()`, `write_text()`, `open()` and `exists()`

## Description

The `pathlib` module allows a Python program to construct and use filesystem
paths. File handling allows the program to work with information stored outside
the program. The usual process is:

```text
file path -> open or read the file -> process the data -> optionally write data
```

A **path** describes where a file is located. It is not the file's contents.
The `Path` class from `pathlib` provides a clear, portable way to construct and
use paths.

## Import

```python
from pathlib import Path
```

## Construct a path beside the Python file

```python
data_file = Path(__file__).resolve().parent / "temperature.txt"
```

- `__file__` is the path of the running Python file.
- `.resolve()` produces an absolute path.
- `.parent` selects the folder containing the Python file.
- `/ "temperature.txt"` adds the filename to that folder path.

For example, if the Python file is `C:\Github_repos\test.py`, the constructed
path is `C:\Github_repos\temperature.txt`.

> [!NOTE]
> `__file__` is normally available in a saved Python script. It may not be
> available when entering instructions directly into an interactive console.

## Reading and writing methods

| Method | Purpose | Important behaviour |
|---|---|---|
| `read_text()` | Read the entire file as one string | The file must exist |
| `write_text()` | Create a file and write a string | Overwrites existing contents |
| `open("a")` | Open a file and append text | Preserves existing contents |
| `exists()` | Check whether a path exists | Returns `True` or `False` |

Use `encoding="utf-8"` for predictable handling of ordinary text and symbols.

## Example 1: Read comma-separated integers

Suppose `temperature.txt` contains:

```text
10, 20, 30, 25, 28
```

Read and convert the values:

```python
from pathlib import Path

data_file = Path(__file__).resolve().parent / "temperature.txt"
text = data_file.read_text(encoding="utf-8")
items = text.split(",")
temperatures = [int(item) for item in items]

print(temperatures)
```

Output:

```text
[10, 20, 30, 25, 28]
```

The types change during the process:

```text
Path -> string -> list of strings -> list of integers
```

`int()` accepts the spaces around values such as `" 20"`. For other types of
text data, `.strip()` can remove surrounding spaces explicitly.

## Example 2: Create a file and write text

```python
from pathlib import Path

output_file = Path(__file__).resolve().parent / "notes.txt"
message = "Temperature measurement completed.\n"

output_file.write_text(message, encoding="utf-8")
```

If `notes.txt` does not exist, Python creates it. If it already exists,
`write_text()` replaces its previous contents.

> [!WARNING]
> Check the path carefully before using `write_text()` with an important file,
> because overwriting removes the old contents.

## Example 3: Append data without overwriting

```python
from pathlib import Path

output_file = Path(__file__).resolve().parent / "notes.txt"

with output_file.open("a", encoding="utf-8") as file:
    file.write("A second measurement was added.\n")
```

The mode `"a"` means **append**. New text is added at the end of the file. The
`with` statement closes the file automatically, including when an error occurs.

## Common file modes

| Mode | Meaning | If the file is missing | If the file exists |
|---|---|---|---|
| `"r"` | Read | Raises an error | Reads it |
| `"w"` | Write | Creates it | Overwrites it |
| `"a"` | Append | Creates it | Adds to the end |
| `"x"` | Create only | Creates it | Raises an error |

## Writing a list as comma-separated data

`write_text()` accepts a string, so numbers must first be converted to text:

```python
from pathlib import Path

temperatures = [10, 20, 30, 25, 28]
text = ", ".join(str(value) for value in temperatures)

data_file = Path(__file__).resolve().parent / "temperature.txt"
data_file.write_text(text, encoding="utf-8")
```

The stored file contains:

```text
10, 20, 30, 25, 28
```

## Check before reading

```python
if data_file.exists():
    text = data_file.read_text(encoding="utf-8")
else:
    print("The data file was not found.")
```

This is useful when a missing file is expected. If the file should always be
present, allowing `FileNotFoundError` to appear can make a mistake easier to
diagnose.

## Common mistakes

- Treating a `Path` object as though it contains the file's data.
- Appending a filename to `__file__` without first selecting `.parent`.
- Using `.parents[1]` when the required file is in the same folder.
- Forgetting that `read_text()` returns a string.
- Passing integers directly to `write_text()` instead of converting them to
  text.
- Using `write_text()` or mode `"w"` when the old contents must be preserved.
- Depending on the terminal's current folder instead of constructing a path
  relative to the script.

## When to use CSV or JSON

Comma-separated text is sufficient for a small one-dimensional list. For rows
and columns, use Python's standard-library `csv` module. For structured data
containing names, lists and settings, use the standard-library `json` module.

## See also

- [`split()`](../strings/methods/split_method.md)
- [`int`](../data-types/int_datatype.md)
- [`str`](../data-types/str_datatype.md)
