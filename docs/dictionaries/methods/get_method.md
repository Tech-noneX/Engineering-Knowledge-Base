---

id: get
title: "get()"
section: "Dictionary Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Safely gets the value for a key in a dictionary, returns default if missing"
tags: ["dict", "dictionary", "method", "safe access", "default", "lookup"]
see_also: ["setdefault()", "keys()", "values()", "get() user profile lookup **R.W.E**"]
works_with: ["dict"]

---

# get()

- **Used with:**
Dictionary (`dict`)
- **Construct:**  
Method
- **Library:**  
Built-in
- **Iterable:**  
Yes (but for key access, not value iteration)
- **Time Complexity:**  
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

- **Required:** 1 (`key`)
- **Optional:** 1 (`default`)
- **Maximum:** 2 (`key, default`)

- Required:
  - `key`
  - The dictionary key you want to look up.

```python
d = {"a": 1, "b": 2}
print(d.get("a"))  # Output: 1
```

*Looks for the key "a" and returns its value.*

- Optional:
  - `default`
  - The value to return if the key is not found. Defaults to `None` if not given.

```Python
d = {"a": 1}
print(d.get("z", 100))  # Output: 100
```

*Returns 100 instead of None since "z" is missing.*

- Maximum
  - Two arguments: key (`required`), default (`optional`).

```Python
d = {"a": 1}
print(d.get("b", 0))  # Output: 0
```

*You can use up to two arguments with get()—the key and a default value.*

## Examples

```python
d = {'a': 10, 'b': 20}
print(d.get('a'))         # 10
print(d.get('z'))         # None
print(d.get('z', 999))    # 999
```

## Tips & Common mistakes

- **No KeyError:** Unlike `dict[key]`, `get()` never raises an error if the key doesn't exist.
- Use the `default` parameter to avoid having to check if a key is in the dictionary first.
- Forgetting to use the `default` parameter and assuming you'll always get a value back.
- Thinking `get()` works with lists or other types—it’s for dictionaries only.

```python
my_dict = {"name": "Alice"}

# Common mistake: forgetting to use default
age = my_dict.get("age")
print(age)  # Output: None (might cause bugs if you expect an int)
print(age + 1)  # ❌ TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
```

## See Also

- [`setdefault()`](setdefault)
- [`keys()`](keys)
- [`values()`](values)
- [`get() user profile lookup` **R.W.E**](get_rwe)
