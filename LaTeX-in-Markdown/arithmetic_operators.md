---
id: latex-arithmetic-operators
title: LaTeX Arithmetic Operators
section: Mathematics
module: LaTeX
difficulty: beginner
subscription: free
reference: Arithmetic operator notation in Markdown using LaTeX
tags:
  - latex
  - markdown
  - arithmetic
  - operators
see_also:
  - latex-fractions-mixed-numbers
  - latex-powers-indices-roots
  - latex-comparison-symbols
works_with:
  - markdown
  - github
  - obsidian
  - mathjax
  - katex
file_path: docs/mathematics/latex/arithmetic_operators.md
---

## LaTeX Arithmetic Operators

| Meaning              | LaTeX code       | Rendered      |
|---                   |---               |---            |
| Addition             | `$a + b$`        | $a+b$         |
| Subtraction          | `$a - b$`        | $a-b$         |
| Multiplication cross | `$a \times b$`   | $a\times b$   |
| Multiplication dot   | `$a \cdot b$`    | $a\cdot b$    |
| Division sign        | `$a \div b$`     | $a\div b$     |
| Fraction division    | `$\frac{a}{b}$`  | $\frac{a}{b}$ |
| Plus or minus        | `$\pm$`          | $\pm$         |
| Minus or plus        | `$\mp$`          | $\mp$         |
| Modulo               | `$a \bmod b$`    | $a\bmod b$    |

## Example

`LaTeX code:`

```markdown
$$
(-4) \times (-4) = 16
$$
```

`rendered:`

>## $(-4) \times (-4) = 16$

## Tips and Common Mistakes

- Use `\times` when the multiplication sign must be visually explicit.
- Use `\cdot` when writing algebraic or vector products.
- Do not use the letter `x` as a multiplication sign.
