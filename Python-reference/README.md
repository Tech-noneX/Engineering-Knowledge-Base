# Python Reference

A structured library of beginner-friendly Python reference cards with a small
command-line browser, reusable Markdown templates and generated metadata.

The project currently contains **53 completed reference cards** across seven
topic categories. It is a working and growing part of the wider Engineering
Knowledge Base, with the long-term goal of supplying content to a Flutter
application.

## Features

- Browse cards through structured topic menus.
- Search all available cards directly by name.
- Open the selected Markdown card in its associated Windows application.
- Keep every card organised with YAML front matter.
- Export card metadata and content to a reusable JSON index.
- Create consistent new cards from the included templates.

## Available Topics

| Topic | Cards | Examples |
|---|---:|---|
| Built-in functions | 14 | `len`, `range`, `enumerate` |
| Data types | 8 | `list`, `dict`, `tuple` |
| Dictionary methods | 1 | `get` |
| List functions and methods | 10 | `append`, `pop`, `sorted` |
| Modules | 2 | `functools`, `reduce` |
| Set methods | 2 | `add`, `union` |
| String methods | 16 | `split`, `strip`, `replace` |
| **Total** | **53** | |

## Project Structure

```text
Python-reference/
|-- app/
|   |-- python_cheat_sheet.py   # Structured CLI card browser
|   |-- md_paths.py             # Paths used by the browser
|   |-- greetings_function.py   # Search-prompt greetings
|   `-- save_metadata.py        # YAML-to-JSON metadata exporter
|-- docs/                       # Markdown cards grouped by topic
|-- metadata/
|   `-- python_metadata.json    # Generated card index
|-- templates/                  # Templates for creating new cards
|-- todolist.md                 # Development roadmap
`-- README.md
```

## Run the Reference Browser

From the root of the Engineering Knowledge Base repository, run:

```powershell
python Python-reference/app/python_cheat_sheet.py
```

The main menu displays the available categories:

```text
+----------------------------------------------------------+
|                 PYTHON REFERENCE BROWSER                 |
+----------------------------------------------------------+
|  53 reference cards available                            |
|                                                          |
|  1  Built-in functions                                   |
|  2  Data types                                           |
|  3  List functions and methods                           |
|  4  String methods                                       |
|  5  Dictionary methods                                   |
|  6  Set methods                                          |
|  7  Modules                                              |
|                                                          |
|  s  Search all cards                                     |
|  q  Quit                                                 |
+----------------------------------------------------------+
```

Choose a numbered topic to see all cards available in that category. Type a
listed name, such as `append`, to open its Markdown card. The category menu
remains active so that another card can be opened afterwards.

### Controls

| Input | Action |
|---|---|
| `1` to `7` | Open a topic menu |
| Card name | Open the corresponding Markdown card |
| `b` | Return to the main menu |
| `s` | Search across every category |
| `help` | Show topics while using global search |
| `q` | Quit from the main menu |

> [!NOTE]
> The browser uses `os.startfile()` to open Markdown files, so the current CLI
> is intended for Windows.

## Configure a Markdown Reader on Windows

The reference cards are Markdown (`.md`) files. To read them with the CLI, you
need a Markdown reader or editor installed on your computer. The project does
not require a specific application; you can use whichever Markdown reader you
prefer.

The CLI asks Windows to open the selected card with the default application
associated with `.md` files. Configure that application before using the
browser:

1. Install the Markdown reader or editor you want to use.
2. Find any `.md` file in File Explorer.
3. Right-click the file and select **Open with**.
4. Select **Choose another app**.
5. Choose your preferred Markdown reader. If it is not shown, select
   **More apps** or **Choose an app on your PC** and locate it manually.
6. Enable **Always use this app to open .md files**.
7. Select **OK**.

After this setup, choosing a card in the Python Reference Browser will open it
automatically in that Markdown reader. To change readers later, repeat the same
steps and choose a different application.

## Reference-Card Format

Each reference card starts with YAML front matter describing information such
as its title, category, difficulty and related topics. This data is intended to
support future search, filtering and cross-reference features.

When creating a card:

1. Start with the appropriate file in [`templates/`](templates/README.md).
2. Save the new Markdown file in the correct folder below `docs/`.
3. Add its path to `app/md_paths.py` and the appropriate browser dictionary.
4. Rebuild the metadata index.

## Rebuild the Metadata Index

The CLI browser uses only the Python standard library. The metadata exporter
additionally requires [PyYAML](https://pyyaml.org/):

```powershell
python -m pip install PyYAML
python Python-reference/app/save_metadata.py
```

The exporter scans the cards in a stable order and writes the generated index
to `metadata/python_metadata.json`.

## Project Status

This Python reference is an active learning project, not a finished Python
documentation replacement. Planned cards and future application features are
tracked in the [`todolist.md`](todolist.md) development roadmap.
