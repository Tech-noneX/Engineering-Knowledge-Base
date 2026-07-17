---
id: functools
title: "functools"
section: "Modules"
module: "standard library"
difficulty: intermediate
subscription: premium
reference: "Higher-order functions and utilities for functional programming and decorators"
tags: [ "standard library", "functional", "decorator", "caching", "tools" ]
see_also: [ "itertools", "operator", "collections" ]
works_with: [ "function", "callable", "iterable" ]
file_path: Python-reference/docs/modules/functools/functools_module.md
---

# functools

- **Category:** Standard Library
- **Installation & Import:**  
  No installation needed (built-in since Python 2.5+)
- **Common Use Cases:**  
  Functional programming tools, decorators, caching, function manipulation, partial application, performance optimization.
- **Key Classes/Functions:**  
  `lru_cache`, `wraps`, `partial`, `reduce`, `cached_property`, `total_ordering`, `singledispatch`, `cmp_to_key`
- **Time Complexity:**  
  Varies by function (e.g., `lru_cache` is O(1) for cache hit, O(n) for miss in worst case; `reduce` is O(n))

## Description

`functools` is a standard library module providing higher-order functions and operations on callable objects.  
It supports functional programming techniques in Python, like function composition, decorators, memoization (caching), and advanced function transformations.

- Use `functools` for:
  - Function decorators (e.g., `wraps`)
  - Memoization/caching (`lru_cache`, `cache`)
  - Adapting function signatures (`partial`)
  - Implementing custom ordering (`total_ordering`)
  - Advanced dispatching (`singledispatch`)
  - Utilities for working with callables

## Usable With

- **Python Version:** 2.5+ (most features), some (like `cached_property`, `cache`) require Python 3.8+ or 3.9+
- Works with any Python function, method, or callable object.
- Useful in data processing, performance-critical code, decorators, and code requiring functional techniques.

```diff
- Python Version: 3.9+ recommended for all features (partial features in 3.2+, 3.8+)
```

```diff
- platform: Cross-platform (Windows, MacOS, Linux)
```

## Import Syntax

```python
import functools
from functools import lru_cache, wraps, partial
```

- **explanation:**  
  Import the full module or just the function(s) you need.  
  No pip install required; standard with Python.

## Key Functions & Classes

- `lru_cache(maxsize=128)`: Decorator for least-recently-used caching of function results.
- `wraps(wrapper)`: Decorator to make decorated functions preserve metadata (name, docstring, etc.).
- `partial(func, *args, **kwargs)`: Return a new function with some arguments fixed.
- `reduce(function, iterable[, initializer])`: Apply a function cumulatively to reduce an iterable to a single value.
- `cached_property`: Decorator that converts a method into a cached property (Python 3.8+).
- `total_ordering`: Class decorator for filling in missing rich comparison methods.
- `singledispatch`: Create single-dispatch generic functions (function overloading based on argument type).
- `cmp_to_key(func)`: Convert old-style comparison functions to key functions for sorting.

## Examples

- **Basic import and use**

```python
from functools import lru_cache

@lru_cache(maxsize=100)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))  # Output: 55
```

- **Common real-world pattern**

```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # Output: 25
```

- **Advanced/lesser-known feature**

```python
from functools import total_ordering

@total_ordering
class Box:
    def __init__(self, volume):
        self.volume = volume
    def __eq__(self, other):
        return self.volume == other.volume
    def __lt__(self, other):
        return self.volume < other.volume

# Now Box supports all rich comparisons
```

- **Edge-case**

```python
from functools import reduce

# Reducing an empty iterable without an initializer raises TypeError
try:
    result = reduce(lambda x, y: x + y, [])
except TypeError:
    result = "Error: empty sequence with no initial value"
print(result)
```

**Note:**  
Some features (like `cached_property`) require Python 3.8+, and `cache` requires 3.9+.  
`lru_cache` can grow memory if not bounded or cleared periodically.

## Tips & Common mistakes

- `@wraps` should always be used in custom decorators to avoid losing function metadata.
- Use `lru_cache` only on pure functions (same input = same output, no side effects).
- `reduce` is in `functools` in Python 3 (not built-in as in Python 2); always `from functools import reduce`.
- Setting `maxsize=None` in `lru_cache` creates an unbounded cache—risk of memory leaks.
- `partial` does not replace arguments already passed at call-time—explicitly set them as needed.

```python
# Common mistake: not using @wraps in a decorator
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # do something
        return func(*args, **kwargs)
    return wrapper
```

## See Also

- `itertools` (advanced iteration)
- `operator` (function versions of common operators)
- `collections` (namedtuple, defaultdict, etc.)
