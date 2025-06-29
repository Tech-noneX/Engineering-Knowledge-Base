---
id: get
title: "get()"
section: "Dictionary Methods"
tags: ["dict", "dictionary", "method", "safe access", "default", "lookup"]
see_also: ["[]", "setdefault()", "keys()", "values()"]
works_with: ["dict"]
---

# get()

**Used with:**
Dictionary `dict`

  **Construct:**  
Method

  **Library:**  
Built-in

  **Iterable:**  
Yes (but for key access, not value iteration)

  **Time Complexity:**  
Average: O(1) (constant time lookup)

## Description

`get()` is a dictionary method that retrieves the value for a given key if it exists in the dictionary.  
Unlike the standard bracket access (`dict[key]`), `get()` will **not raise a KeyError** if the key does not exist—it returns a default value instead (or `None` if not specified).

**Common use:**  
Safely retrieve a value from a dictionary when you're not sure the key is present.

## Usable With

- All Python dictionaries.

## Syntax

```python
dictionary.get(key, default=None)
```

- `key` (required): The key to look up.
- `default` (optional): The value to return if `key` is not found. If not provided, returns `None`.

## Arguments

| Argument | Type         | Required | Default | Description                      |
| -------- | ------------ | -------- | ------- | -------------------------------- |
| key      | any hashable | Yes      |         | Key to search for                |
| default  | any          | No       | None    | Value to return if key not found |

## Examples

```python
d = {'a': 10, 'b': 20}
print(d.get('a'))         # 10
print(d.get('z'))         # None
print(d.get('z', 999))    # 999
```

## Tips

- **No KeyError:** Unlike `dict[key]`, `get()` never raises an error if the key doesn't exist.
- Use the `default` parameter to avoid having to check if a key is in the dictionary first.

## Common Mistakes

- Forgetting to use the `default` parameter and assuming you'll always get a value back.
- Thinking `get()` works with lists or other types—it’s for dictionaries only.

## See Also

- `setdefault()` (adds key with default if missing)
- Bracket access `[]`
- `keys()`, `values()`
