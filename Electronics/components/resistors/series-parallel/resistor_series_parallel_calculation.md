# Resistance, Voltage drop, Current calculation

## Schematics

![Series-parallel resistor schematic](resistors_series_parallel_combined.svg)

## Resistors

$R_1 = 125\Omega$

$R_2 = 150\Omega$

$R_3 = 150\Omega$

$R_4 = 300\Omega$

$R_5 = 1\,k\Omega$

$R_6 = 2\,k\Omega$

$R_7 = 500\Omega$

## Power

$V = 9VDC$

## Circuit analysis

Resistors in parallel have to be calculate first, we can split them in two groups-$R_{b}$ where:

$R_{b1} = R_4\,||\,R_5$

$R_{b2} = R_6\,||\,R_7$

Then $R_{b1}$ equivalent can be treated as a resistor as well as $R_{b2}$ equivalent.

Then we do simple calculation of $R_{b3} = R_{b1} + R_{b2}$  because they connected in series.

After that we calculate resistors $R_{s1} = R_2 + R_3$

Now we have last parallel calculation $R_{eq} = R_{s1}\,||\,R_{b3}$

Finally $\boxed{R_{total} = R_1 + R_{eq}}$
