<div align="center">

# 🗂️ Python — more data structures: sets, dictionaries

**Sets, dictionaries — and the moment you stop looping over what you can map.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

Lists are ordered; the real power moves start here. **Dictionaries** give
you key → value mapping, and **sets** give you O(1) membership and one-line
algebra (`&` intersection, `|` union). The tasks also push toward
**functional style**: `map()`, `lambda`, `sorted()` with keys — ending with a
Roman numeral converter that rewards careful dictionary design.

## 🎯 Concepts covered

- Dictionaries: keys, values, `get()`, sorted iteration
- Sets: intersection, union, uniqueness for free
- `map()` + `lambda` — transforming without loops
- `sorted()` with a `key=` function (weight averages, scores)
- Complex deletes: removing keys by value
- Roman numerals → integers, the dictionary way

## 📂 Files

| File | What it does |
|---|---|
| [`0-square_matrix_simple.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/0-square_matrix_simple.py) | Returns the square of every value in a 2D matrix |
| [`1-search_replace.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/1-search_replace.py) | Replaces all occurrences of an element in a list |
| [`10-best_score.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/10-best_score.py) | Returns the key with the biggest value — or None |
| [`100-weight_average.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/100-weight_average.py) | Weighted average of a list of `(score, weight)` tuples |
| [`101-square_matrix_map.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/101-square_matrix_map.py) | Squares a matrix — the functional `map`-only version |
| [`102-complex_delete.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/102-complex_delete.py) | Deletes every dictionary key whose value matches |
| [`11-multiply_list_map.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/11-multiply_list_map.py) | Maps a function over a list *without* a loop |
| [`12-roman_to_int.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/12-roman_to_int.py) | Converts a Roman numeral string to an integer |
| [`2-uniq_add.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/2-uniq_add.py) | Sums only the *unique* integers of a list |
| [`3-common_elements.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/3-common_elements.py) | Returns the common elements of two lists (set intersection) |
| [`4-only_diff_elements.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/4-only_diff_elements.py) | Returns elements present in only one of two sets |
| [`5-number_keys.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/5-number_keys.py) | Counts the keys in a dictionary |
| [`6-print_sorted_dictionary.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/6-print_sorted_dictionary.py) | Prints a dictionary by ordered keys |
| [`7-update_dictionary.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/7-update_dictionary.py) | Replaces or adds key/value pairs in a dictionary |
| [`8-simple_delete.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/8-simple_delete.py) | Deletes a key from a dictionary — safely |
| [`9-multiply_by_2.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-more_data_structures/9-multiply_by_2.py) | Returns a new dictionary with values × 2 |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 3-common_elements.py    # set intersection in one line
python3 12-roman_to_int.py      # XIV → 14
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
