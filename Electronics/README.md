# Electronics

Electronics knowledge organized by component. At the moment, this section
contains resistor circuits.

## Structure

```text
Electronics/
`-- components/
    `-- resistors/
        |-- series/
        |-- parallel/
        `-- series-parallel/
```

## Resistor Topics

- [Resistors in series](components/resistors/series/README.md)
- [Resistors in parallel](components/resistors/parallel/README.md)
- [Series-parallel resistors](components/resistors/series-parallel/README.md)

Every topic folder keeps its related Markdown explanation, Python calculator,
SVG export, and KiCad files together. This makes the engineering context visible
without searching through separate documentation, asset, and example folders.

Run the current series-resistor calculator from the repository root:

```powershell
python Electronics/components/resistors/series/resistors_in_series_calc.py
```

