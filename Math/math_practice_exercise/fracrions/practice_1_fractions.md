
# Practice Exercise 7 Basic Engineering Mathematics

## 1.  $\frac{2}{5}\times\frac{4}{7}$

### `calculation: 1`

```math
\frac{2}{5}\times\frac{4}{7}
=\frac{2\times4}{5\times7}
=\boxed{\frac{8}{35}}
```

`Python Calculation:`

```python
from fractions import Fraction

calculation_fraction = Fraction(2, 5) * Fraction(4, 7)

print(calculation_fraction)

# output 8/35
```


## 2. $5\times\frac{4}{9}$

### `calculation: 2`

```math
5\times\frac{4}{9}
= \frac{5}{1}\times\frac{4}{9}
= \frac{5\times4}{1\times9}
= \frac{20}{9}
= \boxed{2\frac{2}{9}}
```

## 3. $\frac{3}{4}\times\frac{8}{11}$

### `calculation: 3`

```math
\begin{aligned}
\frac{3}{4}\times\frac{8}{11}
&= \frac{3}{\cancel{4}^{1}}\times\frac{\cancel{8}^{2}}{11}\\[6pt]
&= \frac{3\times2}{1\times11}\\[6pt]
&= \boxed{\frac{6}{11}}
\end{aligned}
```

## 4. $\frac{3}{4}\times\frac{5}{9}$

### `calculation: 4`

```math
\begin{aligned}
\frac{3}{4}\times\frac{5}{9}
&=\frac{\cancel{3}^{1}}{4}\times\frac{5}{\cancel{9}^{3}}\\[6pt]
&=\frac{1\times5}{4\times3}\\[6pt]
&=\boxed{\frac{5}{12}}
\end{aligned}
```

## 5. $\frac{17}{35}\times\frac{15}{68}$

### `calculation: 5`

```math
\begin{aligned}
\frac{17}{35}\times\frac{15}{68}
&= \frac{\cancel{17}^{1}}{\cancel{35}^{7}}\times\frac{\cancel{15}^{3}}{\cancel{68}^{4}}\\[6pt]
&= \frac{1\times3}{7\times4}\\[6pt]
&= \boxed{\frac{3}{28}}
\end{aligned}
```

## 6. $\frac{3}{5}\times\frac{7}{9}\times1\frac{2}{7}$

### `calculation: 6`

```math
\begin{aligned}
\frac{3}{5}\times\frac{7}{9}\times1\frac{2}{7}
&= \frac{3}{5}\times\frac{7}{9}\times\frac{9}{7}\\[6pt]
&= \frac{3}{5}\times\frac{\cancel{7}^{1}}{9}\times\frac{9}{\cancel{7}^{1}}\\[6pt]
&= \frac{3}{5}\times\frac{1}{\cancel{9}^{1}}\times\frac{\cancel{9}^{1}}{1}\\[6pt]
&= \frac{3\times1\times1}{{5}\times{1}\times{1}}\\[6pt]
&= \boxed{\frac{3}{5}}
\end{aligned}
```

```python
from fractions import Fraction

calculation_fraction = Fraction(3, 5) * Fraction(7, 9) * Fraction((1*7+2), 7)

print(calculation_fraction)

# output 3/5
```


## 7. $\frac{13}{17}\times4\frac{7}{11}\times3\frac{4}{39}$

### `calculation: 7`

```math
\begin{aligned}
\frac{13}{17}\times4\frac{7}{11}\times3\frac{4}{39}&= \frac{13}{17}\times\frac{51}{11}\times\frac{121}{39}\\[6pt]
&= \frac{13}{\cancel{17}^{1}}\times\frac{\cancel{51}^{3}}{11}\times\frac{121}{39}\\[6pt]
&= \frac{13}{1}\times\frac{3}{\cancel{11}^{1}}\times\frac{\cancel{121}^{11}}{39}\\[6pt]
&= \frac{\cancel{13}^{1}}{1}\times\frac{3}{1}\times\frac{11}{\cancel{39}^{3}}\\[6pt]
&= \frac{1}{1}\times\frac{\cancel{3}^{1}}{1}\times\frac{11}{\cancel{3}^{1}}\\[6pt]
&= \frac{1\times1\times11}{1\times1\times1}\\[6pt]
&= \boxed{11}
\end{aligned}
```

## 8. $\frac{1}{4}\times\frac{3}{11}\times1\frac{5}{39}$

### `calculation: 8`

```math
\begin{aligned}
\frac{1}{4}\times\frac{3}{11}\times1\frac{5}{39}
&= \frac{1}{4}\times\frac{3}{11}\times\frac{44}{39} \\[6pt]
&= \frac{1}{\cancel{4}^{1}}\times\frac{\cancel{3}^{1}}{11}
\times\frac{\cancel{44}^{11}}{\cancel{39}^{13}} \\[6pt]
&= \frac{1}{1}\times\frac{1}{\cancel{11}^{1}}
\times\frac{\cancel{11}^{1}}{13} \\[6pt]
&= \boxed{\frac{1}{13}}
\end{aligned}
```

## 9. $\frac{2}{9}\div\frac{4}{27}$

### `calculation: 9`

```math
\begin{aligned}
\frac{2}{9}\div\frac{4}{27}
&= \frac{2}{9}\times\frac{27}{4} \\[6pt]
&= \frac{\cancel{2}^{1}}{\cancel{9}^{1}}
\times\frac{\cancel{27}^{3}}{\cancel{4}^{2}} \\[6pt]
&= \frac{3}{2} \\[6pt]
&= \boxed{1\frac{1}{2}}
\end{aligned}
```

## 10. $\frac{3}{8}\div\frac{45}{64}$

### `calculation: 10`

```math
\begin{aligned}
\frac{3}{8}\div\frac{45}{64}
&= \frac{3}{8}\times\frac{64}{45} \\[6pt]
&= \frac{\cancel{3}^{1}}{\cancel{8}^{1}}
\times\frac{\cancel{64}^{8}}{\cancel{45}^{15}} \\[6pt]
&= \boxed{\frac{8}{15}}
\end{aligned}
```

## 11. $\frac{3}{8}\div\frac{5}{32}$

### `calculation: 11`

```math
\begin{aligned}
\frac{3}{8}\div\frac{5}{32}
&= \frac{3}{8}\times\frac{32}{5} \\[6pt]
&= \frac{3}{\cancel{8}^{1}}\times\frac{\cancel{32}^{4}}{5} \\[6pt]
&= \frac{12}{5} \\[6pt]
&= \boxed{2\frac{2}{5}}
\end{aligned}
```

## 12. $\frac{3}{4}\div1\frac{4}{5}$

### `calculation: 12`

```math
\begin{aligned}
\frac{3}{4}\div1\frac{4}{5}
&= \frac{3}{4}\div\frac{9}{5} \\[6pt]
&= \frac{3}{4}\times\frac{5}{9} \\[6pt]
&= \frac{\cancel{3}^{1}}{4}\times\frac{5}{\cancel{9}^{3}} \\[6pt]
&= \boxed{\frac{5}{12}}
\end{aligned}
```

## 13. $2\frac{1}{4}\times1\frac{2}{3}$

### `calculation: 13`

```math
\begin{aligned}
2\frac{1}{4}\times1\frac{2}{3}
&= \frac{9}{4}\times\frac{5}{3} \\[6pt]
&= \frac{\cancel{9}^{3}}{4}\times\frac{5}{\cancel{3}^{1}} \\[6pt]
&= \frac{15}{4} \\[6pt]
&= \boxed{3\frac{3}{4}}
\end{aligned}
```

## 14. $1\frac{1}{3}\div2\frac{5}{9}$

### `calculation: 14`

```math
\begin{aligned}
1\frac{1}{3}\div2\frac{5}{9}
&= \frac{4}{3}\div\frac{23}{9} \\[6pt]
&= \frac{4}{3}\times\frac{9}{23} \\[6pt]
&= \frac{4}{\cancel{3}^{1}}\times\frac{\cancel{9}^{3}}{23} \\[6pt]
&= \boxed{\frac{12}{23}}
\end{aligned}
```

## 15. $2\frac{4}{5}\div\frac{7}{10}$

### `calculation: 15`

```math
\begin{aligned}
2\frac{4}{5}\div\frac{7}{10}
&= \frac{14}{5}\div\frac{7}{10} \\[6pt]
&= \frac{14}{5}\times\frac{10}{7} \\[6pt]
&= \frac{\cancel{14}^{2}}{\cancel{5}^{1}}
\times\frac{\cancel{10}^{2}}{\cancel{7}^{1}} \\[6pt]
&= \frac{2\times2}{1\times1} \\[6pt]
&= \boxed{4}
\end{aligned}
```

## 16. $2\frac{3}{4}\div3\frac{2}{3}$

### `calculation: 16`

```math
\begin{aligned}
2\frac{3}{4}\div3\frac{2}{3}
&= \frac{11}{4}\div\frac{11}{3} \\[6pt]
&= \frac{11}{4}\times\frac{3}{11} \\[6pt]
&= \frac{\cancel{11}^{1}}{4}\times\frac{3}{\cancel{11}^{1}} \\[6pt]
&= \boxed{\frac{3}{4}}
\end{aligned}
```

## 17. $\frac{1}{9}\times\frac{3}{4}\times1\frac{1}{3}$

### `calculation: 17`

```math
\begin{aligned}
\frac{1}{9}\times\frac{3}{4}\times1\frac{1}{3}
&= \frac{1}{9}\times\frac{3}{4}\times\frac{4}{3} \\[6pt]
&= \frac{1}{9}\times\frac{\cancel{3}^{1}}{\cancel{4}^{1}}
\times\frac{\cancel{4}^{1}}{\cancel{3}^{1}} \\[6pt]
&= \frac{1}{9}\times\frac{1}{1}\times\frac{1}{1} \\[6pt]
&= \boxed{\frac{1}{9}}
\end{aligned}
```

## 18. $3\frac{1}{4}\times1\frac{3}{5}\div\frac{2}{5}$

### `calculation: 18`

```math
\begin{aligned}
3\frac{1}{4}\times1\frac{3}{5}\div\frac{2}{5}
&= \frac{13}{4}\times\frac{8}{5}\div\frac{2}{5} \\[6pt]
&= \frac{13}{4}\times\frac{8}{5}\times\frac{5}{2} \\[6pt]
&= \frac{13}{\cancel{4}^{1}}\times\frac{\cancel{8}^{2}}{5}
\times\frac{5}{2} \\[6pt]
&= \frac{13}{1}\times\frac{\cancel{2}^{1}}{\cancel{5}^{1}}
\times\frac{\cancel{5}^{1}}{\cancel{2}^{1}} \\[6pt]
&= \boxed{13}
\end{aligned}
```
