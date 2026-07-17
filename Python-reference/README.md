# Python Reference

A structured Python reference-card library with templates, generated metadata,
and a small Windows CLI search tool for opening the cards.

The library currently contains **53 completed Python reference cards** across
seven topic categories. It is a working, growing knowledge base rather than a
finished interactive application.

## Structure

```text
Python-reference/
|-- app/          # Browser and metadata-generation scripts
|-- docs/         # Markdown reference cards grouped by Python topic
|-- metadata/     # Generated JSON index
|-- templates/    # Reusable reference-card templates
|-- todolist.md
`-- README.md
```

## Available Topics

- `builtins/` - built-in functions such as `len()`, `range()`, and `zip()`
- `data-types/` - Python's core data types
- `dictionaries/` - dictionary methods
- `lists/` - list functions and methods
- `modules/` - standard-library modules
- `sets/` - set methods
- `strings/` - string methods

Each reference card begins with YAML front matter. The metadata supports search,
cross-references, difficulty filters, and future use in a Flutter application.
New cards should start from a file in [`templates/`](templates/README.md).

## Run the Cheat-Sheet Browser

From the repository root:

```powershell
python Python-reference/app/python_cheat_sheet.py
```

Choose a numbered topic to browse its available cards, then enter a listed name
such as `list`, `append`, `len`, or `filter` to open it. Enter `b` to return to
the main menu, `s` to search all cards directly, or `q` to quit. The CLI opens
the matching Markdown card in your associated application. It uses
`os.startfile`, so it is currently intended for Windows.

## Rebuild the Metadata Index

The metadata exporter requires PyYAML:

```powershell
python -m pip install PyYAML
python Python-reference/app/save_metadata.py
```

The generated index is saved as `metadata/python_metadata.json`.
