# Engineering Knowledge Base

A structured, long-term record of my journey from electrician to software,
embedded, automation, and electrical/electronics engineering.

The repository combines beginner-friendly reference cards with practical code,
engineering calculations, visualizations, schematics, and small learning
projects. Its content-first architecture keeps the material useful as Markdown
today and suitable for a future Flutter application.

## Knowledge Areas

- [Python](docs/python/README.md)
- [Electronics](docs/electronics/README.md)
- [Mathematics](docs/mathematics/README.md)
- [C](docs/c/README.md)
- [C++](docs/cpp/README.md)
- [MicroPython](docs/micropython/README.md)
- [Embedded systems](docs/embedded-systems/README.md)
- [Electrical engineering](docs/electrical-engineering/README.md)
- [Automation and PLCs](docs/automation/README.md)

The Python and electronics sections currently contain the most material. Other
sections provide a clean foundation for future notes and projects.

## Repository Architecture

```text
Engineering-Knowledge-Base/
|-- docs/                 # Reference cards and engineering explanations
|   |-- python/
|   |-- electronics/
|   |-- mathematics/
|   |-- c/
|   |-- cpp/
|   |-- micropython/
|   |-- embedded-systems/
|   |-- electrical-engineering/
|   `-- automation/
|-- templates/            # Reusable Markdown card templates
|-- assets/               # Images, diagrams, and schematic source files
|-- examples/             # Small programs and worked engineering examples
|-- scripts/              # Tools that maintain or browse the knowledge base
|-- LICENSE
`-- README.md
```

## How Content Is Organized

The repository separates different kinds of material deliberately:

- `docs/` explains concepts and acts as the main knowledge library.
- `templates/` keeps new reference cards consistent.
- `assets/` stores supporting visual and schematic files.
- `examples/` contains runnable code and worked calculations.
- `scripts/` contains repository tools rather than learning examples.

Python reference cards retain YAML front matter for search, filtering, and
future application use. Fields such as `id`, `title`, `section`, `difficulty`,
`tags`, `see_also`, and `works_with` should remain machine-readable.

## Working With the Repository

Clone the repository and open it in Visual Studio Code:

```powershell
git clone https://github.com/Tech-noneX/Engineering-Knowledge-Base.git
Set-Location Engineering-Knowledge-Base
```

To run the current Windows-oriented Python reference browser:

```powershell
python scripts/python/python_cheat_sheet.py
```

Individual examples include their own instructions or accompanying notes.

## Adding New Material

1. Choose the correct subject and topic folder under `docs/`.
2. Start from the closest matching file in `templates/`.
3. Keep the YAML metadata keys and value types consistent.
4. Put reusable images, diagrams, or schematics under `assets/`.
5. Put runnable demonstrations under `examples/`.
6. Use relative Markdown links and check them after moving files.
7. Keep explanations practical, accurate, and understandable to learners.

## Project Status

This is an evolving learning project. Some subjects are currently placeholders,
while Python and electronics already contain reference material and practical
work. Existing notes will be reviewed and improved as my engineering knowledge
develops.

## License

This project is available under the [MIT License](LICENSE).
