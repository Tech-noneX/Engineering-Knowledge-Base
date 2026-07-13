# Engineering Knowledge Base

A practical record of my learning journey from electrician to software,
embedded, automation, and electrical/electronics engineering.

The repository is intentionally organized by subject and topic. Files that
belong to one engineering topic stay together, making each topic easy to study,
move, expand, and eventually present in a Flutter application.

## Current Structure

```text
Engineering-Knowledge-Base/
|-- Python-reference/
|   |-- app/          # Cheat-sheet browser and metadata tools
|   |-- docs/         # Python reference cards
|   |-- metadata/     # Generated card index
|   `-- templates/    # Python card templates
|-- Electronics/
|   `-- components/
|       `-- resistors/
|           |-- series/
|           |-- parallel/
|           `-- series-parallel/
|-- Math/              # Reserved for future material
|-- C/                 # Reserved for future material
|-- C++/               # Reserved for future material
|-- LICENSE
`-- README.md
```

## Subjects

### [Python reference](Python-reference/README.md)

Structured Markdown cards, YAML metadata, templates, and a small Windows
cheat-sheet browser.

### [Electronics](Electronics/README.md)

Component-based electronics notes. Each resistor topic keeps its explanation,
calculation program, SVG image, and KiCad source files in one folder.

### Future subjects

`Math/`, `C/`, and `C++/` are intentionally empty. Their internal structure will
be created only when real learning material is ready.

## Organization Rule

Keep everything that belongs to one topic together. For example, a series
resistor note, calculator, schematic, PCB file, and exported image all belong in
`Electronics/components/resistors/series/`.

Repository-wide tools are the exception: Python indexing and browsing tools
remain in `Python-reference/app/`, while reusable Python card layouts remain in
`Python-reference/templates/`.

## Running the Python Cheat Sheet

From the repository root:

```powershell
python Python-reference/app/python_cheat_sheet.py
```

## Project Status

Python and resistor-circuit material are currently available. New subjects and
subfolders will be added gradually as the knowledge base grows.

## License

This project is available under the [MIT License](LICENSE).
