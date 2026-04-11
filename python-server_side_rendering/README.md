<div align="center">

# 🖨️ Python — server-side rendering

**Flask + Jinja2: HTML assembled on the server, before the browser ever sees it.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Jinja2](https://img.shields.io/badge/template-Jinja2-B41717?style=flat-square)](https://jinja.palletsprojects.com)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

Server-side rendering is the original web: the server builds the finished
HTML and the browser just displays it. This project walks the full SSR
stack — a Flask route returning plain text, then **Jinja2 templates** with
variables and conditionals, then feeding templates from **files** (CSV,
JSON), and finally rendering from a real **SQLite database**.

The `templates/` folder tells the story visually: `base.html` with header &
footer partials, and child pages that extend it — template inheritance,
the pattern every bigger framework borrows.

## 🎯 Concepts covered

- Flask routes, `app.run()`, and the dev server
- `render_template` — passing Python into HTML
- Jinja2 logic: `{% if %}`, `{% for %}`, filters
- Template inheritance: `extends`, `block`, partials
- Reading CSV / JSON as template data sources
- SQLite + `sqlite3` as a rendering backend

## 📂 Files

| File | What it does |
|---|---|
| [`create_database.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/create_database.py) | Builds `products.db` from the product data |
| [`items.json`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/items.json) | Item list used by the templates |
| [`products.csv`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/products.csv) | Product catalog as CSV |
| [`products.db`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/products.db) | Products |
| [`products.json`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/products.json) | Product catalog as JSON |
| [`requirements.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/requirements.txt) | Requirements |
| [`task_00_intro.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/task_00_intro.py) | The hello-world Flask route — where every web app starts |
| [`task_01_jinja.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/task_01_jinja.py) | First `render_template` — variables injected into HTML |
| [`task_02_logic.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/task_02_logic.py) | Jinja2 conditionals & loops — dynamic pages from data |
| [`task_03_files.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/task_03_files.py) | Templates fed from CSV and JSON files |
| [`task_04_db.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/task_04_db.py) | Templates rendered from a SQLite query |
| [`template.txt`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/template.txt) | Template |
| [`templates/about.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/about.html) | About page |
| [`templates/base.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/base.html) | The layout skeleton every page extends |
| [`templates/contact.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/contact.html) | Contact page |
| [`templates/footer.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/footer.html) | Shared footer partial |
| [`templates/header.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/header.html) | Shared header partial |
| [`templates/index.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/index.html) | Home page — extends `base.html` |
| [`templates/items.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/items.html) | Renders the items list |
| [`templates/product_display.html`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-server_side_rendering/templates/product_display.html) | One product, rendered from the database |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 🐍 Flask (see `requirements.txt`) and `sqlite3`
- 🧹 Style: pycodestyle (PEP 8)

## 🚀 Try it yourself

```bash
pip3 install -r requirements.txt
python3 task_00_intro.py          # → http://127.0.0.1:5000
python3 task_04_db.py             # renders rows straight from SQLite
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
