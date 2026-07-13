"""Export Python reference-card metadata to JSON."""

import json
from pathlib import Path
from typing import Any

import yaml


REPOSITORY_ROOT = Path(__file__).resolve().parents[2]
CARDS_ROOT = REPOSITORY_ROOT / "docs" / "python"
OUTPUT_JSON = CARDS_ROOT / "metadata" / "python_metadata.json"


def extract_card(markdown_path: Path) -> dict[str, Any] | None:
    """Return a card's metadata and content, or None for a normal Markdown page."""
    text = markdown_path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None

    parts = text.split("---", 2)
    if len(parts) < 3:
        raise ValueError(f"Unclosed YAML front matter: {markdown_path}")

    metadata = yaml.safe_load(parts[1]) or {}
    if not isinstance(metadata, dict):
        raise TypeError(f"YAML front matter must be a mapping: {markdown_path}")

    metadata["content"] = parts[2].strip()
    metadata["file_path"] = markdown_path.relative_to(REPOSITORY_ROOT).as_posix()
    return metadata


def scan_cards(cards_root: Path) -> list[dict[str, Any]]:
    """Read all reference cards below cards_root in a stable order."""
    cards = []
    for markdown_path in sorted(cards_root.rglob("*.md")):
        card = extract_card(markdown_path)
        if card is not None:
            cards.append(card)
    return cards


def main() -> None:
    """Generate the metadata index used by knowledge-base tooling."""
    cards = scan_cards(CARDS_ROOT)
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(
        json.dumps(cards, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"Exported {len(cards)} cards to {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
