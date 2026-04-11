<div align="center">

# 🧠 Python — everything is object

**The philosophy exam: 28 questions on identity, equality and mutability.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

No functions to write this time — this project is a **Q&A deep-dive into
Python's object model**. Every `N-answer.txt` answers a question like *“what
does `id(a) == id(b)` really mean?”*, comparing aliasing versus copying,
`is` versus `==`, why small integers are cached, and which types silently
mutate while others never do.

The few code files are the payoff: a `magic_string` class attribute trick
and a `LockedClass` that forbids new attributes — only `first_name` and
`__last_name` allowed.

## 🎯 Concepts covered

- `is` (identity) vs `==` (equality) vs `type()`
- Aliasing: one object, many names
- Mutability of lists, dicts, sets vs strings & tuples
- Why `a += [1]` and `a = a + [1]` behave differently
- Small-int caching and string interning
- `id()` — what object identity really means
- `__slots__`-style locking via custom classes

## 📂 Files

| File | What it does |
|---|---|
| [`0-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/0-answer.txt) | Answer |
| [`1-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/1-answer.txt) | Answer |
| [`10-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/10-answer.txt) | Answer |
| [`100-magic_string.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/100-magic_string.py) | Returns a string whose class attribute counts calls — `Best School` × N |
| [`101-locked_class.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/101-locked_class.py) | `LockedClass` — no new attributes beyond `first_name` / `__last_name` |
| [`103-line1.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/103-line1.txt) | Line1 |
| [`103-line2.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/103-line2.txt) | Line2 |
| [`104-line1.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/104-line1.txt) | Line1 |
| [`104-line2.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/104-line2.txt) | Line2 |
| [`104-line3.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/104-line3.txt) | Line3 |
| [`104-line4.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/104-line4.txt) | Line4 |
| [`104-line5.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/104-line5.txt) | Line5 |
| [`105-line1.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/105-line1.txt) | Line1 |
| [`106-line1.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/106-line1.txt) | Line1 |
| [`106-line2.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/106-line2.txt) | Line2 |
| [`106-line3.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/106-line3.txt) | Line3 |
| [`106-line4.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/106-line4.txt) | Line4 |
| [`106-line5.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/106-line5.txt) | Line5 |
| [`11-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/11-answer.txt) | Answer |
| [`12-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/12-answer.txt) | Answer |
| [`13-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/13-answer.txt) | Answer |
| [`14-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/14-answer.txt) | Answer |
| [`15-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/15-answer.txt) | Answer |
| [`16-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/16-answer.txt) | Answer |
| [`17-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/17-answer.txt) | Answer |
| [`18-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/18-answer.txt) | Answer |
| [`19-copy_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/19-copy_list.py) | Returns a *copy* of a list — the aliasing antidote |
| [`2-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/2-answer.txt) | Answer |
| [`20-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/20-answer.txt) | Answer |
| [`21-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/21-answer.txt) | Answer |
| [`22-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/22-answer.txt) | Answer |
| [`23-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/23-answer.txt) | Answer |
| [`24-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/24-answer.txt) | Answer |
| [`25-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/25-answer.txt) | Answer |
| [`26-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/26-answer.txt) | Answer |
| [`27-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/27-answer.txt) | Answer |
| [`28-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/28-answer.txt) | Answer |
| [`3-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/3-answer.txt) | Answer |
| [`4-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/4-answer.txt) | Answer |
| [`5-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/5-answer.txt) | Answer |
| [`6-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/6-answer.txt) | Answer |
| [`7-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/7-answer.txt) | Answer |
| [`8-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/8-answer.txt) | Answer |
| [`9-answer.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/9-answer.txt) | Answer |
| [`tests/100-main.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/tests/100-main.py) | Tests/100-main |
| [`tests/101-main.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/tests/101-main.py) | Tests/101-main |
| [`tests/19-main.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-everything_is_object/tests/19-main.py) | Tests/19-main |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
python3 -c "a = [1]; b = a; b.append(2); print(a)"   # why does a change?
python3 -c "print(id(1) == id(1), 256 is 256)"       # small int caching
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
