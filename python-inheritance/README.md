<div align="center">

# 🧬 Python — inheritance

**Stop rewriting classes — extend them: BaseGeometry, Rectangle, Square, MyInt.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

Inheritance is how class libraries avoid copy-paste. This project builds a
small type hierarchy: `BaseGeometry` validates integers (raising clean
exceptions), `Rectangle` inherits it, `Square` inherits `Rectangle` — and
`MyInt` inherits `int` just to rebel and invert `==`.

Along the way it covers the introspection trio — `isinstance()`,
`type()` exact checks, and a custom `inherits_from()` — plus the lookup of
every attribute and method a class exposes.

## 🎯 Concepts covered

- `class Child(Parent)` — inheriting attributes and methods
- `super()` and overriding inherited behavior
- `isinstance()` vs exact `type()` checks
- Custom `inherits_from()` — without `isinstance`
- Raising clean exceptions from validators
- Overriding operators in subclasses (`MyInt` flips `==`)

## 📂 Files

| File | What it does |
|---|---|
| [`0-lookup.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/0-lookup.py) | Returns the list of attributes & methods of an object |
| [`1-my_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/1-my_list.py) | `MyList` extends `list` with a `print_sorted()` method |
| [`10-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/10-square.py) | `Square` inherits `Rectangle` — one size to rule them |
| [`100-my_int.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/100-my_int.py) | `MyInt` — an int subclass with an *inverted* `==` |
| [`101-add_attribute.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/101-add_attribute.py) | Adds an attribute to an object — or raises TypeError if it can't |
| [`11-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/11-square.py) | Square's own `__str__` — `[Square] size/size` |
| [`2-is_same_class.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/2-is_same_class.py) | Exact type check — same class, subclasses need not apply |
| [`3-is_kind_of_class.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/3-is_kind_of_class.py) | `is_kind_of_class` — a reimplementation of `isinstance` |
| [`4-inherits_from.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/4-inherits_from.py) | True if the object inherits (but isn't) the given class |
| [`5-base_geometry.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/5-base_geometry.py) | An empty `BaseGeometry` class |
| [`6-base_geometry.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/6-base_geometry.py) | Adds `area()` — which raises a clean Exception |
| [`7-base_geometry.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/7-base_geometry.py) | Adds `integer_validator(name, value)` |
| [`8-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/8-rectangle.py) | `Rectangle` inherits `BaseGeometry` — width, height, validation |
| [`9-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/9-rectangle.py) | Adds `area()` and a `__str__` — `[Rectangle] width/height` |
| [`tests/1-my_list.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/tests/1-my_list.txt) | Tests/1-my list |
| [`tests/7-base_geometry.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-inheritance/tests/7-base_geometry.txt) | Tests/7-base geometry |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 -i 8-rectangle.py
>>> r = Rectangle(4, 3); r.area()
12
python3 -i 100-my_int.py
>>> MyInt(1) == 1      # rebellious subclass: False
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
