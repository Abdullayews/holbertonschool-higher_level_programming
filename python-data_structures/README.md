<div align="center">

# 📊 Python — data structures: lists, tuples

**Lists and tuples — the workhorse containers of Python.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

Sequences are the first *real* data structures: ordered, indexable,
sliceable. This project is a tour of **lists** (mutable) and **tuples**
(immutable) through a set of surgical little functions — indexing safely,
replacing elements, printing in reverse, iterating matrices, and swapping
variables the Pythonic way: with a tuple.

## 🎯 Concepts covered

- Lists: indexing, slicing, `len()`, iteration
- Mutability — replacing an element without breaking the original list
- Tuples: packing & unpacking, tuple assignment (`a, b = b, a`)
- Functions returning multiple values (they're tuples!)
- 2D lists — printing a matrix of integers
- Booleans as a list: mapping a divisibility test

## 📂 Files

| File | What it does |
|---|---|
| [`0-print_list_integer.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/0-print_list_integer.py) | Prints each integer of a list, one per line |
| [`1-element_at.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/1-element_at.py) | Retrieves an element at an index — safely (None if out of range) |
| [`10-divisible_by_2.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/10-divisible_by_2.py) | Returns a list of booleans — which elements are divisible by 2 |
| [`11-delete_at.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/11-delete_at.py) | Deletes the item at a given position, safely |
| [`12-switch.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/12-switch.py) | Swaps the values of `a` and `b` using tuple assignment |
| [`2-replace_in_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/2-replace_in_list.py) | Replaces an element at a specific position |
| [`3-print_reversed_list_integer.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/3-print_reversed_list_integer.py) | Prints the list in reverse order (integer by integer) |
| [`4-new_in_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/4-new_in_list.py) | Returns a *new* list with an element replaced — original untouched |
| [`5-no_c.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/5-no_c.py) | Removes every `c` and `C` from a string |
| [`6-print_matrix_integer.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/6-print_matrix_integer.py) | Prints a matrix of integers, neatly aligned |
| [`7-add_tuple.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/7-add_tuple.py) | Adds two tuples element-wise |
| [`8-multiple_returns.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/8-multiple_returns.py) | Returns a tuple: (length of sentence, first character) |
| [`9-max_integer.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-data_structures/9-max_integer.py) | Finds the biggest integer in a list |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 10-divisible_by_2.py    # which elements are multiples of 2?
python3 12-switch.py            # tuple swap: a and b trade places
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
