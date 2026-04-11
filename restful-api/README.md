<div align="center">

# 🌐 RESTful API

**From raw sockets to Flask endpoints — with a taste of security.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=flat-square&logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![HTTP](https://img.shields.io/badge/protocol-HTTP%2F1.1-005C84?style=flat-square)](https://developer.mozilla.org/en-US/docs/Web/HTTP)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

REST is the grammar of the modern web — and this project learns it from
the bottom up. First with the **`requests`** library as a client, then by
building an **HTTP server by hand on raw sockets**, parsing request lines
and headers the way the protocol actually defines them.

Then the pragmatic layer: **Flask** turning routes into a clean JSON API,
and finally a first look at **securing** it — because an open endpoint is
an invitation.

## 🎯 Concepts covered

- HTTP methods: GET, POST, PUT, DELETE — the resource verbs
- Status codes: 200, 201, 301, 404, 500 — speaking fluent HTTP
- The `requests` library as an API client
- Raw sockets: parsing an HTTP request by hand
- Flask routes returning JSON
- Basic API security concepts

## 📂 Files

| File | What it does |
|---|---|
| [`task_02_requests.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/restful-api/task_02_requests.py) | Consuming an API with `requests` — the client's view |
| [`task_03_http_server.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/restful-api/task_03_http_server.py) | An HTTP server built on raw sockets, no framework |
| [`task_04_flask.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/restful-api/task_04_flask.py) | A RESTful API with Flask routes and JSON responses |
| [`task_05_basic_security.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/restful-api/task_05_basic_security.py) | First steps in locking an API down |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 🐍 `requests` and `Flask` from `requirements.txt`-style installs
- 🧹 Style: pycodestyle (PEP 8)

## 🚀 Try it yourself

```bash
python3 task_03_http_server.py    # hand-rolled HTTP server on a socket
python3 task_04_flask.py          # the same idea, written the Flask way
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
