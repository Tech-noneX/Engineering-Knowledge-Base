# Repository Scripts

Tools that browse, index, validate, or maintain the Engineering Knowledge Base.
These are repository utilities rather than standalone learning examples.

## Python Reference Browser

The files in `python/` provide the current Windows-oriented reference browser
and metadata helper.

From the repository root:

```powershell
python scripts/python/python_cheat_sheet.py
```

Enter the name of a supported Python concept to open its reference card, or
enter `q` to quit.

## Metadata Export

`python/save_metadata.py` rebuilds the JSON metadata index from the YAML front
matter in the Python reference cards. It requires PyYAML:

```powershell
python -m pip install PyYAML
python scripts/python/save_metadata.py
```
