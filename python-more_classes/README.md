<div align="center">

# 📐 Python — more classes

**The Rectangle, perfected — dunders, class methods, and the N-Queens boss fight.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

One class, ten iterations: the `Rectangle` starts empty and ends up with
private validated attributes, `area()` / `perimeter()`, `__str__` drawing,
`__repr__` for `eval()` round-trips, `__del__` farewell messages, class
attributes counting instances, static methods comparing two rectangles, and
a class method building squares.

Then, as a bonus: **the N-Queens puzzle** — placing N non-attacking queens
on an N×N board with a recursive backtracking solver.

## 🎯 Concepts covered

- Class attributes vs instance attributes
- Class methods (`@classmethod`) and static methods (`@staticmethod`)
- More dunders: `__str__`, `__repr__`, `__del__`
- `print_symbol` — a class attribute as a customization hook
- Solving N-Queens with recursion + backtracking

## 📂 Files

| File | What it does |
|---|---|
| [`0-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/0-rectangle.py) | An empty `Rectangle` class with a class attribute |
| [`1-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/1-rectangle.py) | Private, validated `width` / `height` with getters & setters |
| [`101-nqueens.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/101-nqueens.py) | The N-Queens solver — all solutions for a given board size |
| [`2-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/2-rectangle.py) | Adds `area()` and `perimeter()` |
| [`3-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/3-rectangle.py) | `__str__` draws the rectangle with `#` |
| [`4-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/4-rectangle.py) | `__repr__` — `eval()` can rebuild the object from its text |
| [`5-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/5-rectangle.py) | A class attribute + a `__del__` goodbye message |
| [`6-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/6-rectangle.py) | Tracks `number_of_instances` across creations and deletions |
| [`7-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/7-rectangle.py) | `print_symbol` class attribute — draw with any character |
| [`8-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/8-rectangle.py) | Static method: which rectangle is bigger (or equal)? |
| [`9-rectangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_classes/9-rectangle.py) | Class method `square(cls, size)` — rectangles from one number |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 101-nqueens.py 6     # every valid arrangement of 6 queens
python3 -c "from models.rectangle import Rectangle; print(Rectangle(4,3))"
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
