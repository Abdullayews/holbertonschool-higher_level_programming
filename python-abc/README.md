<div align="center">

# 🧩 Python — abstract base classes

**ABCs, duck typing and multiple inheritance — the polite way to share skeletons.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![abc](https://img.shields.io/badge/module-abc%20%C2%B7%20abc.abstractmethod-3776AB?style=flat-square)](https://docs.python.org/3/library/abc.html)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

Abstract Base Classes answer the question *“how do I force subclasses to
implement a method — without writing the implementation?”*. This project
builds `ABC` parents with `@abstractmethod`, then contrasts them with **duck
typing** — if it quacks, who cares about the class hierarchy?

The showpiece is multiple inheritance done carefully: a `FlyingFish` that
inherits from both `Fish` and `Bird` ABCs without method collisions, and a
`Dragon` mixing even more ancestors — each parent contributing exactly the
behavior it owns.

## 🎯 Concepts covered

- `ABC` and `@abstractmethod` — unimplemented-by-design methods
- Duck typing: behavior over type
- Multiple inheritance and method resolution order (MRO)
- Overriding inherited methods
- Containers you subclass yourself: `VerboseList`, `CountedIterator`

## 📂 Files

| File | What it does |
|---|---|
| [`task_00_abc.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-abc/task_00_abc.py) | An abstract class with an abstract `area()` — instantiating it fails loudly |
| [`task_01_duck_typing.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-abc/task_01_duck_typing.py) | Same behavior, no inheritance — duck typing demonstrated |
| [`task_02_verboselist.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-abc/task_02_verboselist.py) | `VerboseList` extends `list` and announces every append/remove |
| [`task_03_countediterator.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-abc/task_03_countediterator.py) | An iterator that counts how many items you consumed |
| [`task_04_flyingfish.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-abc/task_04_flyingfish.py) | `FlyingFish` — multiple inheritance from `Fish` and `Bird` ABCs |
| [`task_05_dragon.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-abc/task_05_dragon.py) | `Dragon` — a multi-parent class pulling swim, fly and crawl together |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 🧹 Style: pycodestyle (PEP 8)
- 📚 The `abc` module is the star of the show

## 🚀 Try it yourself

```bash
python3 task_02_verboselist.py    # a list that narrates every mutation
python3 task_04_flyingfish.py     # Fish + Bird → FlyingFish
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
