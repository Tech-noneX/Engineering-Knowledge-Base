import os
import json
import yaml

def extract_metadata_and_content(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()
    # Split YAML front matter and content
    if text.startswith('---'):
        parts = text.split('---', 2)
        if len(parts) >= 3:
            meta, content = parts[1], parts[2]
            metadata = yaml.safe_load(meta)
        else:
            metadata, content = {}, text
    else:
        metadata, content = {}, text
    # Always add content to metadata as 'content' field
    metadata['content'] = content.strip()
    # Add the relative file path for traceability
    metadata['file_path'] = md_path
    return metadata

def scan_cards(root_dir):
    card_list = []
    for dirpath, dirs, files in os.walk(root_dir):
        for filename in files:
            if filename.endswith('.md'):
                md_path = os.path.join(dirpath, filename)
                card_data = extract_metadata_and_content(md_path)
                card_list.append(card_data)
    return card_list

if __name__ == "__main__":
    # Set this to the root folder of your cards (e.g., 'Python-cheat-sheet')
    CARDS_ROOT = "Python-cheat-sheet"
    OUTPUT_JSON = os.path.join(CARDS_ROOT, "meta-data", "python_metadata.json")

    all_cards = scan_cards(CARDS_ROOT)
    with open(OUTPUT_JSON, 'w', encoding='utf-8') as f:
        json.dump(all_cards, f, indent=2, ensure_ascii=False)

    print(f"Exported {len(all_cards)} cards to {OUTPUT_JSON}")
