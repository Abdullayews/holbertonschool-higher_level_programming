<div align="center">

# 📮 Python — serialization

**Saving objects for later: JSON, pickle, CSV, XML — and over the wire.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Formats](https://img.shields.io/badge/formats-JSON%20%C2%B7%20pickle%20%C2%B7%20CSV%20%C2%B7%20XML-8E75B2?style=flat-square)](#)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

Serialization is the translation layer between live objects and bytes you
can store or send. This project walks the format spectrum: **JSON** for
portability, **pickle** for full Python object fidelity (and its risks),
**CSV** for spreadsheets, **XML** for the enterprise corner — and finally
sending data **over a network socket**.

Each format gets the same treatment: save an object, load it back, verify
nothing was lost in translation.

## 🎯 Concepts covered

- JSON — the universal interchange format
- `pickle` — serializing anything Python (and why you never unpickle strangers)
- CSV — tables, headers, `csv.DictReader`
- XML — element trees and namespaces
- Sockets — sending serialized bytes over the network
- Choosing a format: portability vs fidelity vs size

## 📂 Files

| File | What it does |
|---|---|
| [`task_00_basic_serialization.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-serialization/task_00_basic_serialization.py) | Save & load a dictionary as JSON — the warm-up |
| [`task_01_pickle.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-serialization/task_01_pickle.py) | Full-fidelity object persistence with `pickle` |
| [`task_02_csv.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-serialization/task_02_csv.py) | Reading and writing CSV — rows, headers, dialects |
| [`task_03_xml.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-serialization/task_03_xml.py) | XML round-trip: build, serialize, parse back |
| [`task_04_net.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-serialization/task_04_net.py) | Serialize data and ship it over a network socket |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 🧹 Style: pycodestyle (PEP 8)

## 🚀 Try it yourself

```bash
python3 task_01_pickle.py     # an object survives death-by-exit via pickle
python3 task_03_xml.py        # build → serialize → parse back an XML tree
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
