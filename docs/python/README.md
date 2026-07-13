# Python Knowledge Base

Beginner-friendly Python reference cards organized for both human study and
future use by software such as a Flutter knowledge-base application.

## Topics

- `builtins/` - Python's built-in functions
- `data-types/` - core types such as `int`, `str`, `list`, and `dict`
- `dictionaries/` - dictionary operations and methods
- `lists/` - list functions and methods
- `strings/` - string operations and methods
- `sets/` - set operations and methods
- `tuples/` - tuple material
- `modules/` - standard-library modules
- `loops/` - iteration concepts and patterns
- `functions/` - defining and using functions
- `oop/` - object-oriented programming
- `real-world-examples/` - larger examples that connect multiple concepts
- `metadata/` - generated index data used by repository tools

## Reference-Card Format

Each completed reference card starts with YAML front matter. This metadata
supports consistent navigation and allows future applications to search and
filter the content without parsing the whole article.

```yaml
---
id: len
title: "len()"
section: "Built-in Functions"
difficulty: beginner
tags: ["built-in", "function", "length"]
see_also: ["sum()", "list", "str"]
works_with: ["list", "tuple", "str", "dict"]
---
```

Do not rename metadata keys casually. Application code may eventually depend on
them. New cards should start from the matching file in
[`templates/`](../../templates/README.md).

## Python Reference Browser

The repository includes a small Windows-oriented command-line browser. From the
repository root, run:

```powershell
python scripts/python/python_cheat_sheet.py
```

It accepts a topic such as `list`, `append`, `len`, or `filter` and opens the
matching Markdown card. Enter `q` to quit.

## Current Scope

The collection currently covers core data types, built-in functions, list and
string methods, dictionary and set methods, and part of the `functools` module.
The remaining directories are foundations for later study.

