# Electronics Knowledge Base

Practical notes about electronics, circuit theory, components, measurements,
schematics, and calculation methods.

## Sections

- `fundamentals/` - voltage, current, resistance, power, and core laws
- `components/` - resistors, capacitors, diodes, transistors, and other parts
- `circuits/` - analysis of complete circuits and worked calculations
- `measurements/` - instruments, measurement methods, accuracy, and safety
- `schematics/` - explanations of schematic conventions and design choices

## Current Resistor Material

The first practical section covers:

- [resistors in series](circuits/resistors/series/resistor_series_calc.md)
- [resistors in parallel](circuits/resistors/parallel/resistors_in_parallel.md)
- combined series-parallel circuit schematics
- Ohm's law, total resistance, circuit current, and voltage drop
- Python-assisted engineering calculations
- KiCad schematic and PCB practice

The source schematics and SVG exports are stored in
[`assets/schematics/electronics/resistors/`](../../assets/schematics/electronics/resistors/).
The runnable series-resistor calculator is stored in
[`examples/electronics/resistors/series/`](../../examples/electronics/resistors/series/).

Run the calculator from the repository root:

```powershell
python examples/electronics/resistors/series/resistors_in_series_calc.py
```

## Planned Growth

Future material will include semiconductor components, sensors, power supplies,
measurement techniques, microcontrollers, communication buses, PCB design, and
the electronics used in embedded and automation projects.
