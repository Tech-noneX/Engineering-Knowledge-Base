# Engineering Knowledge Base

A long-term, beginner-friendly engineering reference that documents a learning
journey from electrical installation work into software, electronics, embedded
systems, automation, and multidisciplinary engineering.

The repository combines concise reference cards with practical programs,
calculations, visualizations, schematics, and small learning projects. Content
is organized so it can be studied directly in Markdown today and reused by a
future Flutter application.

## Current Areas

### [Python reference](Python%20reference/README.md)

Structured Python reference cards, reusable Markdown templates, metadata, and
small helper programs. The cards cover topics such as data types, built-in
functions, collections, methods, modules, and common programming patterns.

### [Electronics](electronics/Resistors/README.md)

Practical electronics notes, resistor calculations, Python examples, and KiCad
schematics for series, parallel, and combined circuits.

## Repository Structure

```text
Engineering-Knowledge-Base/
|-- Python reference/
|   |-- app/          # Helper programs and future tooling
|   |-- docs/         # Markdown reference cards grouped by topic
|   |-- meta-data/    # Structured metadata for discovery and applications
|   `-- templates/    # Reusable card templates
|-- electronics/
|   `-- Resistors/    # Notes, calculations, and schematics
`-- README.md
```

Additional subject areas will be introduced as separate top-level folders as
the knowledge base grows. Planned areas include C, C++, Embedded C,
MicroPython, mathematics, electrical engineering, embedded systems,
PLC/automation, networking, computer science, and AI fundamentals.

## Content Principles

- Keep explanations accurate, practical, and approachable for learners.
- Preserve YAML front matter so reference cards remain machine-readable.
- Build new cards from the existing templates for consistent structure.
- Prefer small, reusable examples over large unrelated scripts.
- Store source schematics and calculations alongside their explanations.
- Maintain relative links when files or topic folders are reorganized.
- Separate source material from generated files, caches, and local tooling.

## Using the Knowledge Base

Browse the topic folders directly on GitHub, or clone the repository and open
the Markdown files in an editor such as Visual Studio Code.

The Python lookup helper is Windows-oriented. From the `Python reference`
folder, run:

```powershell
python app/python_cheat_sheet.py
```

## Project Status

This is an evolving learning repository. Some sections are more complete than
others, and existing material will be reviewed and improved as knowledge and
engineering experience grow.
