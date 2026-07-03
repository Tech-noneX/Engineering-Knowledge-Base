# Python Cheat Sheet

A beginner-friendly Python reference project with Markdown notes and a small command-line launcher for opening them.

The project is organized around Python topics such as data types, built-in functions, list methods, string methods, dictionary methods, set methods, and the `functools` module.

## Project Structure

```text
Python-cheat-sheet/
+-- app/
|   +-- python_cheat_sheet.py
|   +-- md_paths.py
|   +-- greetings_function.py
|   +-- save_metadata.py
+-- docs/
|   +-- builtins/
|   +-- datatypes/
|   +-- dictionaries/
|   +-- lists/
|   +-- modules/
|   +-- sets/
|   +-- strings/
+-- templates/
+-- meta-data/
```

## How It Works

`app/python_cheat_sheet.py` asks what Python concept you want to look up. If the term is known, it opens the matching Markdown file from `docs/`.

Examples of searchable terms include:

- `list`, `dict`, `str`, `tuple`
- `append`, `sort`, `sorted`, `get`
- `upper`, `lower`, `replace`, `strip`
- `len`, `sum`, `range`, `zip`, `map`, `filter`
- `reduce`, `functools`

## How To Run

From the project folder:

```bash
python app/python_cheat_sheet.py
```

Enter `q` to quit the lookup prompt.

## Notes

- The launcher uses `os.startfile`, so it is designed for Windows.
- The Markdown notes can also be opened directly from the `docs/` folder.
