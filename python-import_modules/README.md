<div align="center">

# 📦 Python — import & modules

**Code you can reuse: modules, imports, argv and the magic of __name__.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)
[![Style](https://img.shields.io/badge/style-pycodestyle_2.7-306998?style=flat-square)](https://pypi.org/project/pycodestyle/)

</div>

---

## 📖 About this project

One file is a script; many files are a system. This project is about
splitting logic into **modules** and pulling it back together with `import` and
`from … import …` — including the classic `if __name__ == "__main__":` guard
that lets a file be both a library *and* a program.

It also goes one level lower than most courses bother with: reading
**bytecode with `dis`**, and reconstructing a function from its disassembly —
plus command-line math with `sys.argv`.

## 🎯 Concepts covered

- `import` vs `from module import name`
- The `if __name__ == "__main__":` idiom
- `sys.argv` — reading command-line arguments
- Modules as namespaces: `module.function`
- Introspection with `dir()`
- Python bytecode and the `dis` disassembler

## 📂 Files

| File | What it does |
|---|---|
| [`0-add.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/0-add.py) | Imports a function from another module and prints its result |
| [`1-calculation.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/1-calculation.py) | Same idea, different module layout — `from` import |
| [`100-my_calculator.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/100-my_calculator.py) | A tiny calculator driven entirely by `sys.argv` + operators module |
| [`101-easy_print.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/101-easy_print.py) | Prints without calling `print` — `__import__` tricks |
| [`102-magic_calculation.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/102-magic_calculation.py) | A function reconstructed from its bytecode disassembly |
| [`103-fast_alphabet.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/103-fast_alphabet.py) | Prints the alphabet in uppercase — the fast, string-module way |
| [`2-args.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/2-args.py) | Prints the number of, and list of, command-line arguments |
| [`3-infinite_add.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/3-infinite_add.py) | Adds every argument passed on the command line |
| [`5-variable_load.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-import_modules/5-variable_load.py) | Imports a variable from a module at runtime |

## ⚙️ Requirements


- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 📄 All files start with the shebang `#!/usr/bin/python3` and end with a new line
- 🧹 Style: **pycodestyle** (PEP 8), version 2.7.*
- 🚫 No imports unless a task explicitly allows them


## 🚀 Try it yourself

```bash
./3-infinite_add.py 10 20 30      # adds every argument: 60
python3 -c "import dis; dis.dis(open('102-magic_calculation.py').read())"
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
