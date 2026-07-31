---
id: latex-brackets-grouping
title: LaTeX Brackets and Grouping
section: Mathematics
module: LaTeX
difficulty: beginner
subscription: free
reference: Bracket, absolute-value, and grouping notation in Markdown using LaTeX
tags:
  - latex
  - markdown
  - brackets
  - grouping
see_also:
  - latex-fractions-mixed-numbers
  - latex-powers-indices-roots
  - latex-vectors
works_with:
  - markdown
  - github
  - obsidian
  - mathjax
  - katex
file_path: docs/mathematics/latex/brackets_and_grouping.md
---

## LaTeX Brackets and Grouping

| Meaning           | LaTeX code         | Rendered         |
|---                |---                 |---               |
| Round brackets    | `$(a+b)$`          | $(a+b)$          |
| Square brackets   | `$[a+b]$`          | $[a+b]$          |
| Curly braces      | `$\{a+b\}$`        | $\{a+b\}$        |
| Absolute value    | `$\lvert x\rvert$` | $\lvert x\rvert$ |
| Magnitude or norm | `$\lVert v\rVert$` | $\lVert v\rVert$ |

## Automatically Sized Brackets

`LaTeX code:`

```markdown
$$
\left\{\frac{3}{2}\times\left[\frac{(a+b)\times(d-e)}{c}\right]\right\}
```

`rendered:`

> ## $\left\{\frac{3}{2}\times\left[\frac{(a+b)\times(d-e)}{c}\right]\right\}$

## Tips and Common Mistakes

- Use `\left` and `\right` around tall fractions.
- Escape visible curly braces with backslashes.
- Use `\lvert` and `\rvert` for unambiguous absolute-value notation.
