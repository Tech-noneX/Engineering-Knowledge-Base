---
id: latex-fractions-mixed-numbers
title: LaTeX Fractions and Mixed Numbers
section: Mathematics
module: LaTeX
difficulty: beginner
subscription: free
reference: Fraction and mixed-number notation in Markdown using LaTeX
tags:
  - latex
  - markdown
  - fractions
  - mixed-numbers
see_also:
  - latex-arithmetic-operators
  - latex-powers-indices-roots
  - latex-multiline-equations
works_with:
  - markdown
  - github
  - obsidian
  - mathjax
  - katex
file_path: docs/mathematics/latex/fractions_and_mixed_numbers.md
---

## LaTeX Fractions and Mixed Numbers

| Meaning                           | LaTeX code                           | Rendered                          |
|---                                |---                                   |---                                |
| Basic fraction                    | `$\frac{1}{2}$`                      | $\frac{1}{2}$                     |
| Mixed number                      | `$3\frac{1}{4}$`                     | $3\frac{1}{4}$                    |
| Improper fraction to mixed number | `$\frac{49}{40}= 1 \frac{9}{40}$`    | $\frac{49}{40}=1\frac{9}{40}$     |
| Nested fraction                   | `$\frac{\frac{1}{2}}{\frac{3}{4}}$`  | $\frac{\frac{1}{2}}{\frac{3}{4}}$ |

## Example

`LaTeX code:`

```markdown
$\frac {3 \frac{5}{10} \div \frac{1}{2}} {\frac{8}{12} \times 6 \frac{1}{10}}$
```

`Rendered:`

>## $\frac{3\frac{5}{10}\, \div\, \frac{1}{2}}{\frac{8}{12}\, \times\,6\frac{1}{10}} = 1\frac{44}{61}$

## Tips and Common Mistakes

- Place the numerator and denominator inside separate braces.
- Write mixed numbers without a multiplication symbol: `3\frac{1}{4}`.
- Use display maths for long fraction calculations.
