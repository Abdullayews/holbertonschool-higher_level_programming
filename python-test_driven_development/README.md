<div align="center">

# 🧪 Python — test-driven development

**Write the test first. Watch it fail. Make it pass. Repeat.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![doctest](https://img.shields.io/badge/tests-doctest%20%C2%B7%20unittest-2DA5C0?style=flat-square)](https://docs.python.org/3/library/doctest.html)

</div>

---

## 📖 About this project

This project flips the workflow: for every task the **test comes first**,
and the code only exists to satisfy it. Half the exercises arrive as failing
`doctest` files — docstrings that double as executable tests — so the loop
becomes *red* → *green* → *refactor*.

The functions themselves are the classics: type-checked `add_integer`,
`matrix_divided` with overflowed rounding, `say_my_name`, `print_square`,
`text_indentation` with its punctuation rules — and matrix multiplication
twice: by hand, then with NumPy.

## 🎯 Concepts covered

- Test-driven development: red → green → refactor
- `doctest` — docstrings that are tests
- `unittest` — the standard library's xUnit framework
- Writing docstrings that document *and* verify
- Type & value validation as seen by the tests
- NumPy vs manual matrix multiplication

## 📂 Files

| File | What it does |
|---|---|
| [`0-add_integer.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/0-add_integer.py) | `add_integer(a, b=98)` — ints only, floats cast, errors raised |
| [`100-matrix_mul.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/100-matrix_mul.py) | Matrix multiplication implemented by hand |
| [`101-lazy_matrix_mul.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/101-lazy_matrix_mul.py) | Same result — delegated to NumPy's `matmul` |
| [`2-matrix_divided.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/2-matrix_divided.py) | Divides a matrix by a number — every edge case handled |
| [`3-say_my_name.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/3-say_my_name.py) | Prints `My name is <first> <last>` — validates both |
| [`4-print_square.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/4-print_square.py) | Prints a square of `#` for a given integer size |
| [`5-text_indentation.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/5-text_indentation.py) | Splits text at `.`, `?`, `:` into two-newline paragraphs |
| [`tests/0-add_integer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/0-add_integer.txt) | Tests/0-add integer |
| [`tests/100-matrix_mul.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/100-matrix_mul.txt) | Tests/100-matrix mul |
| [`tests/101-lazy_matrix_mul.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/101-lazy_matrix_mul.txt) | Tests/101-lazy matrix mul |
| [`tests/2-matrix_divided.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/2-matrix_divided.txt) | Tests/2-matrix divided |
| [`tests/3-say_my_name.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/3-say_my_name.txt) | Tests/3-say my name |
| [`tests/4-print_square.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/4-print_square.txt) | Tests/4-print square |
| [`tests/5-text_indentation.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/5-text_indentation.txt) | Tests/5-text indentation |
| [`tests/6-max_integer_test.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-test_driven_development/tests/6-max_integer_test.py) | A full `unittest` suite for `max_integer` |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 -m doctest ./tests/0-add_integer.txt -v     # verbose doctest run
python3 -m unittest tests.6-max_integer_test         # unittest run
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
