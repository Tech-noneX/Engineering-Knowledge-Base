# sorted

**Used with:**  
Any iterable (lists, tuples, strings, dictionaries, sets, etc.)  
**Construct:**  
Function  
**Library:**  
Built-in  
**Iterable:**  
Yes (returns a new sorted iterable)  
**Time Complexity:**  
O(n log n) (Timsort, average and worst-case)

## Description

Returns a new sorted list from the items in any iterable.  
Unlike `.sort()`, it does **not modify** the original object.

## Usable With

All iterables: lists, tuples, strings, dictionaries (sorts keys), sets, etc.

## Syntax

```python
sorted(iterable, *, key=None, reverse=False)
```

- **explanation:**
  - `iterable`: The object you want to sort (e.g., list, tuple, string, set, dictionary keys).
  - `key=None`: (Optional) A function that extracts a comparison key from each element (e.g., `key=len`).
  - `reverse=False`: (Optional) Set to `True` to sort in descending order.
  - The asterisk `*` means all following arguments must be specified by keyword.
  - **Returns a new sorted list**—original iterable is not modified.

## Arguments

**Required:** 1 (`iterable`)  
**Optional:** 2 (`key`, `reverse`)  
**Maximum:** 3

- Required:

```python
# The iterable to sort.
sorted([3, 1, 2])
sorted('hello')
```

- Optional:

```python
key      # (Optional) Function for custom sort order.
# Example:
sorted(['pear', ' 'apple', 'banana'], key=len)  # Sort by length

reverse  # (Optional) Sort in descending order.
# Example:
sorted([1, 2, 3], reverse=True)  # [3, 2, 1]
```

- Maximum

```python
# All three arguments can be used together.
sorted(['pear', 'apple', 'banana'], key=len, reverse=True)  # ['banana', 'apple', 'pear']
```

## Examples

- **Sort a list of numbers (ascending)**

```python
numbers = [5, 2, 9, 1]
result = sorted(numbers)
# result is [1, 2, 5, 9]
```

- **Sort a string (returns sorted list of characters)**

```python
letters = 'edcba'
result = sorted(letters)
# result is ['a', 'b', 'c', 'd', 'e']
```

- **Sort dictionary keys**

```python
d = {'c': 1, 'b': 2, 'a': 3}
result = sorted(d)
# result is ['a', 'b', 'c']
```

- **Sort with key and reverse (longest to shortest string)**

```python
words = ['pear', 'apple', 'banana']
result = sorted(words, key=len, reverse=True)
# result is ['banana', 'apple', 'pear']
```

 **Note:**  
- `sorted()` always returns a **new list**, even if input is another type.  
- The original iterable is never modified.

## Tips & Common mistakes

- Does **not modify** the original iterable.
- Returns a **list**, even if input is a tuple, set, etc.
- For in-place sorting of lists, use `.sort()` method instead.
- The `key` argument can be any function that takes one argument.
- Sorting a dictionary sorts the keys (not values).

```python
# Incorrect: expecting original to change!
numbers = [3, 1, 2]
sorted(numbers)
print(numbers)  # [3, 1, 2], original is unchanged
```
