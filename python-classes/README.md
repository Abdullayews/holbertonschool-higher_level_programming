<div align="center">

# 🏗️ Python — classes & objects

**Your first custom types: attributes, getters, setters and a square made of #.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

Everything in Python is an object — here you finally get to *author* one.
The project grows a `Square` class task by task: private attributes (name
mangling with `__`), validation with exceptions, getters and setters,
`position` for pretty printing, and the dunder methods `__str__` /
`__repr__` that make objects printable.

The bonus tasks go further: a fully sorted **singly linked list** and
squares that can be *compared* to each other by area.

## 🎯 Concepts covered

- `class` vs `instance`, attributes and methods
- Private attributes via `__name` mangling
- Getter / setter patterns with property validation
- `__str__` and `__repr__` — making objects printable
- Instantiating with default and positional arguments
- Comparing objects: `__eq__`, `__lt__`, area-based ordering

## 📂 Files

| File | What it does |
|---|---|
| [`0-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/0-square.py) | An empty `Square` class — everyone starts somewhere |
| [`1-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/1-square.py) | Private `__size` + `area()` method |
| [`100-singly_linked_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/100-singly_linked_list.py) | `Node` + `SinglyLinkedList` with sorted `add` and `__str__` printing |
| [`101-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/101-square.py) | Square with `__str__` — `print(square)` draws it |
| [`102-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/102-square.py) | Squares that compare: `__eq__`, `__lt__` and friends by area |
| [`2-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/2-square.py) | Size validation — `TypeError` / `ValueError` on bad input |
| [`3-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/3-square.py) | Adds the size getter |
| [`4-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/4-square.py) | Adds the setter — with the same validation |
| [`5-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/5-square.py) | Prints the square as a grid of `#` |
| [`6-square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-classes/6-square.py) | Adds a `position` offset for printing |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 -i 4-square.py
>>> Square(5).area()
25
# run 0-square.py → 6-square.py in order and watch the class grow
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
