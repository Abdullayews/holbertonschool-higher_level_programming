<div align="center">

# 🔄 Python — input/output

**Files, JSON and the class-to-dict pipeline that feeds them.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![JSON](https://img.shields.io/badge/format-JSON-000000?style=flat-square&logo=json&logoColor=white)](https://www.json.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

Programs that forget everything when they exit are goldfish. This project
builds the memory: reading and writing files with `with`, appending without
truncating, and — the main act — **JSON round-trips**: `json.dumps` /
`json.loads`, saving class instances via their `__dict__`, and reloading
students from disk.

The bonus tasks end with a log-parsing script that reads server logs from
stdin and computes traffic statistics — I/O in the real world.

## 🎯 Concepts covered

- `open()` in `with` blocks — files that close themselves
- Read / write / append modes
- `json.dumps()` / `json.loads()` — serialization & deserialization
- Saving objects: `__dict__` and `to_json()`
- Reading from stdin line by line
- Pascal's triangle — generated, then written out

## 📂 Files

| File | What it does |
|---|---|
| [`0-read_file.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/0-read_file.py) | Reads a UTF-8 text file and prints it — the `with` way |
| [`1-write_file.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/1-write_file.py) | Writes a string to a file, returns the character count |
| [`10-student.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/10-student.py) | Reloads attributes from a dict — `reload_from_json()` |
| [`100-append_after.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/100-append_after.py) | Inserts a line of text after any line containing a search string |
| [`101-stats.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/101-stats.py) | Reads logs from stdin, computes total size and status-code counts |
| [`11-student.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/11-student.py) | `to_json()` with attribute filtering |
| [`12-pascal_triangle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/12-pascal_triangle.py) | Returns the first `n` rows of Pascal's triangle |
| [`2-append_write.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/2-append_write.py) | Appends text without destroying what was there |
| [`3-to_json_string.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/3-to_json_string.py) | Serializes any object with a `__dict__` to a JSON string |
| [`4-from_json_string.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/4-from_json_string.py) | Deserializes a JSON string back into a Python object |
| [`5-save_to_json_file.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/5-save_to_json_file.py) | Writes an object to a file as JSON |
| [`6-load_from_json_file.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/6-load_from_json_file.py) | Creates an object from a JSON file |
| [`7-add_item.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/7-add_item.py) | Adds command-line arguments to a JSON list that persists between runs |
| [`8-class_to_json.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/8-class_to_json.py) | Returns the dictionary description of a class instance |
| [`9-student.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-input_output/9-student.py) | `Student` with `to_json()` — pick your attributes |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 🧹 Style: pycodestyle (PEP 8)
- 🔗 `json` and `sys` — the two imports everything leans on

## 🚀 Try it yourself

```bash
./7-add_item.py hello world       # argv items accumulate in add_item.json
python3 12-pascal_triangle.py     # rows of Pascal's triangle
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
