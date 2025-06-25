# append()

## Description

The `append()` method adds a single item to the end of a **list**.  
It is one of the most common list methods in Python.
Can be used in loops.

## Usable With

- **Data type:** Only works with lists (`list`)
- **Data structures:** Standard Python lists (not sets, not tuples, not strings, not dictionaries)

## Syntax

```python
list.append(item)
```

## Examples

- **Appending an integer to a list**

```python
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)   # Output: [1, 2, 3, 4]
```

- **Appending string to a list**

```python
words = ["apple", "banana"]
words.append("cherry")
print(words)     # Output: ['apple', 'banana', 'cherry']
```

- **Appending list as a single item**

```python
fruits = ["apple", "banana"]
fruits.append(["orange", "grape"])
print(fruits)    # Output: ['apple', 'banana', ['orange', 'grape']]
```

 **Note: append() adds the entire object as one element. If you want to add multiple elements, use extend() instead.**

## Tips & Common mistakes

- **Only lists have `append()`**. Other data structures like tuples and sets do NOT have this method.
- `append()` **modifies the original list** in place and returns `None`.
- To add more than one element, use `extend()`:

```python
numbers = [1, 2]
numbers.extend([3, 4])
print(numbers)  # Output: [1, 2, 3, 4]
```
