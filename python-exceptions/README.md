<div align="center">

# 🛟 Python — exceptions

**Fail gracefully: try, except, else, finally — and never crash mid-print.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

A program that crashes on bad input is a demo; one that survives it is a
product. This project builds the defensive layer: every function wraps its
work in `try` / `except`, catches exactly the right error (`TypeError`,
`ValueError`, `IndexError`, `ZeroDivisionError`) and returns a safe value
instead of exploding.

The final boss is again bytecode: rebuilding a `magic_calculation` function
from its disassembly — with exceptions inside.

## 🎯 Concepts covered

- `try` / `except` / `else` / `finally` — the full dance
- Catching specific exceptions (never bare `except:`)
- Raising exceptions manually: `raise`, with messages
- Printing errors to `stderr`
- Safe printing of lists, integers and divisions
- Reading bytecode (`dis`) to rebuild exception flow

## 📂 Files

| File | What it does |
|---|---|
| [`0-safe_print_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/0-safe_print_list.py) | Prints `x` elements of a list — never crashes on short lists |
| [`1-safe_print_integer.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/1-safe_print_integer.py) | Prints an integer only if it really is one (`{:d}` formatting) |
| [`100-safe_print_integer_err.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/100-safe_print_integer_err.py) | Prints an integer or writes the error to stderr |
| [`101-safe_function.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/101-safe_function.py) | Executes any function safely — returns its result or None |
| [`102-magic_calculation.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/102-magic_calculation.py) | Reconstructed from bytecode — exceptions and all |
| [`2-safe_print_list_integers.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/2-safe_print_list_integers.py) | Prints only the integers of a mixed list |
| [`3-safe_print_division.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/3-safe_print_division.py) | Safe print division |
| [`4-list_division.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/4-list_division.py) | Element-wise division of two lists with per-element error handling |
| [`5-raise_exception.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/5-raise_exception.py) | Raises a `TypeError` — that's the whole job |
| [`6-raise_exception_msg.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-exceptions/6-raise_exception_msg.py) | Raises a `NameError` with a custom message |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 3-safe_print_division.py    # prints a/b — None on ZeroDivisionError
python3 5-raise_exception.py        # raises a plain TypeError on purpose
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
