---
id: sort
title: "sort()"
section: "List Methods"
module: "built-in"
difficulty: beginner
subscription: free
reference: "Sorts the items of a list in place; original list is changed"
tags: ["list", "method", "in-place", "sort", "mutable", "order"]
see_also: ["sorted()", "reverse()", "pop()", "sort()", "sort() leaderboard update **R.W.E**"]
works_with: ["list"]
file_path: Python-reference/docs/lists/methods/sort_method.md
---

# sort()

- **Used with:**
  lists  
- **Construct:**
  Method  
- **Library:**
 Built-in  
- **Iterable:**
 Yes (the list itself is sorted in place)  
- **Time Complexity:**
 O(n log n)

## Description

Sorts the items of a list in ascending order by default.  
This method sorts the list **in place** and returns `None`.

## Usable With

Python `list` objects.

## Syntax

```python
list.sort(*, key=None, reverse=False)
```

## Arguments

**Required:** 0  
**Optional:** 2 (keyword-only: `key`, `reverse`)  
**Maximum:** 2

- Required:

```python
# No required positional arguments.
# Example:
numbers = [3, 1, 2]
numbers.sort()  # sorts in ascending order
```

- Optional:

```python
key      # (Optional) Function to extract a comparison key from each list element.
# Example:
words = ['pear', 'apple', 'banana']
words.sort(key=len)  # sorts by string length

reverse  # (Optional) If True, sorts the list in descending order.
# Example:
numbers = [1, 2, 3]
numbers.sort(reverse=True)  # [3, 2, 1]
```

- Maximum

```python
# Maximum arguments: key and reverse (both optional).
# Example using both:
words = ['pear', 'apple', 'banana']
words.sort(key=len, reverse=True)  # longest to shortest
```

## Examples

- **Sort a list of numbers in ascending order**

```python
numbers = [3, 1, 4, 2]
numbers.sort()
# numbers is now [1, 2, 3, 4]
```

- **Sort in descending order**

```python
numbers = [3, 1, 4, 2]
numbers.sort(reverse=True)
# numbers is now [4, 3, 2, 1]
```

- **Sort using a key function (sort by string length)**

```python
words = ['apple', 'fig', 'banana']
words.sort(key=len)
# words is now ['fig', 'apple', 'banana']
```

- **Sort using both key and reverse**

```python
words = ['apple', 'fig', 'banana']
words.sort(key=len, reverse=True)
# words is now ['banana', 'apple', 'fig']
```

 **Note:**  
`sort()` modifies the original list and **returns `None`**.  
To get a new sorted list without modifying the original, use `sorted()`.

## Tips & Common mistakes

- `sort()` sorts the list in place; **it does NOT return the sorted list**.
- For non-destructive sorting, use `sorted(list)` instead.
- The `key` argument expects a function that takes one argument and returns a value to use for sorting.
- Only works with lists—not with tuples or other iterables.
- Avoid mixing data types in the list; may raise `TypeError`.

```python
# Incorrect usage: returns None!
numbers = [3, 1, 2]
sorted_numbers = numbers.sort()
print(sorted_numbers)  # Output: None
```

## See Also

- [`sorted()`](sorted)  
- [`reverse()`](reverse)
- [`pop()`](pop)
- [`sort() leaderboard update` **R.W.E**](sort_rwe)
