---
id: type
title: 'type()'
section: 'Built-in Functions'
module: 'built-in'
subscription: free
difficulty: beginner
reference: 'Returns the type of an object or creates a new type/class'
tags: ['built-in', 'function', 'type', 'introspection', 'class', 'object', 'reflection']
see_also: ['isinstance()', 'str()', 'print()', 'id()', 'type() custom class **R.W.E**']
works_with: [any object]
file path: 'docs\builtins\type_function.md'
---

# type()

- **Used with:** Any object (variable, value, custom type, etc.)
- **Construct:** function
- **Library:** Built-in
- **Iterable:** No
- **Time Complexity:** O(1) for type checking; creating new types depends on body size

## Description

The `type()` function serves two purposes:

- **(1) Type check:** With one argument, it returns the type/class of the given object.
- **(2) Dynamic type creation:** With three arguments, it creates a new type (class) at runtime (advanced use).

Commonly used to check the type of a variable or object, especially for debugging or introspection.

## Usable With

Use `type()` with any Python object (number, string, list, user-defined class, etc.).  
Advanced: Create new types by passing name, bases, and dict.

## Syntax

```python
type(object)
type(name, bases, dict)
```

- **explanation:**
  - `type(object)`: Returns the type of the given object.
  - `type(name, bases, dict)`: Creates a new class named `name`, inheriting from `bases`, with attributes from `dict`.

## Arguments

- **Required:** 1 (`object`) OR 3 (`name`, `bases`, `dict`)

- **Optional:** None

- **Maximum:** 3

- Required:

```python
x = 7
print(type(x))  # <class 'int'>
```

- Optional:

```python
# No optional arguments; use 1 or 3 required arguments
```

- Maximum:

```python
# Create a new type (advanced)
MyClass = type('MyClass', (object,), {'x': 5})
obj = MyClass()
print(type(obj))         # <class '__main__.MyClass'>
print(obj.x)             # 5
```

## Examples

- **Check the type of a variable**

```python
value = [1, 2, 3]
print(type(value))  # Output: <class 'list'>
```

- **Check the type for custom objects**

```python
class Dog: pass
d = Dog()
print(type(d))  # Output: <class '__main__.Dog'>
```

- **Create a class dynamically**

```python
Person = type('Person', (), {'greet': lambda self: "Hi!"})
p = Person()
print(p.greet())  # Output: Hi!
```

**Note:**  
For most code, use `type(object)` to check types.  
Dynamic class creation is for advanced/rare use cases.

## Tips & Common mistakes

- Prefer `isinstance(obj, t)` for type *comparison* (handles inheritance).
- `type(obj)` returns the object's direct class; won't match subclasses unless using `isinstance()`.
- Creating classes with `type()` is an advanced feature—rarely needed in regular code.
- You can use `type()` to check types of variables, containers, and even functions.

```python
print(type(3.14))       # <class 'float'>
print(type("hi"))       # <class 'str'>
print(type(len))        # <class 'builtin_function_or_method'>
```

## See Also

- [`isinstance()`](isinstance)
- [`str()`](str)
- [`print()`](print)
- [`id()`](id)
- [`type() custom class` **R.W.E**](type_rwe)
