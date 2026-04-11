<div align="center">

# 🔗 Python — object-relational mapping

**SQLAlchemy: where Python classes become MySQL tables.**

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4%2B-D71F00?style=flat-square)](https://www.sqlalchemy.org)
[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

This project replaces hand-written SQL strings with **two generations of
database access**. The first half uses the raw `MySQLdb` driver — SELECTs,
filters, and a memorable lesson on **SQL injection** (the naive
string-formatting task right next to its parameterized fix).

The second half switches to **SQLAlchemy's declarative ORM**: `State` and
`City` classes mapped onto tables, sessions instead of cursors, and
one-to-many `relationship`s you traverse as plain Python attributes —
`state.cities` — while SQLAlchemy writes the SQL behind the curtain.

## 🎯 Concepts covered

- Raw `MySQLdb`: connect, cursor, fetch, close
- SQL injection — and the parameterized query that stops it
- SQLAlchemy declarative base & mapped classes
- Sessions: add, commit, query, update, delete
- `relationship()` — one-to-many without JOIN syntax
- The state ↔ city model pair, end to end

## 📂 Files

| File | What it does |
|---|---|
| [`0-select_states.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/0-select_states.py) | Lists all states from the DB — raw `MySQLdb` SELECT |
| [`1-filter_states.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/1-filter_states.py) | Filters states starting with `N`, sorted |
| [`10-model_state_my_get.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/10-model_state_my_get.py) | Fetch one state by name — clean `sys.argv` handling |
| [`100-relationship_states_cities.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/100-relationship_states_cities.py) | Creates the DB and both tables — relationship edition |
| [`101-relationship_states_cities_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/101-relationship_states_cities_list.py) | Traverses state → cities via relationship attributes |
| [`102-relationship_cities_states_list.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/102-relationship_cities_states_list.py) | Traverses city → state, the other direction |
| [`11-model_state_insert.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/11-model_state_insert.py) | Adds Louisiana through the ORM session |
| [`12-model_state_update_id_2.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/12-model_state_update_id_2.py) | Renames a state — ORM update pattern |
| [`13-model_state_delete_a.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/13-model_state_delete_a.py) | Deletes every state containing `a` |
| [`14-model_city_fetch_by_state.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/14-model_city_fetch_by_state.py) | Prints cities of a state — via the relationship |
| [`2-my_filter_states.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/2-my_filter_states.py) | User-input filter — the *vulnerable* string-format version |
| [`3-my_safe_filter_states.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/3-my_safe_filter_states.py) | Same filter, done with parameterized queries — injection-proof |
| [`4-cities_by_state.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/4-cities_by_state.py) | Joins cities to states, grouped in order |
| [`5-filter_cities.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/5-filter_cities.py) | All cities of a given state, sorted |
| [`7-model_state_fetch_all.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/7-model_state_fetch_all.py) | ORM query — all States, sorted by id |
| [`8-model_state_fetch_first.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/8-model_state_fetch_first.py) | ORM query — the first State, or None |
| [`9-model_state_filter_a.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/9-model_state_filter_a.py) | States containing the letter `a`, via ORM |
| [`model_city.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/model_city.py) | The `City` class, mapped and linked |
| [`model_state.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/model_state.py) | The `State` class — SQLAlchemy declarative mapping |
| [`relationship_city.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/relationship_city.py) | `City` mapped to `states.id` |
| [`relationship_state.py`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/python-object_relational_mapping/relationship_state.py) | `State` with a `cities` relationship |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · `python3` (3.8.*)
- 🗄️ MySQL 8.0 installed locally (username & password from environment)
- 🐍 `MySQLdb` (`mysqlclient`) and `SQLAlchemy` 1.4.x
- 🧹 Style: pycodestyle (PEP 8)

## 🚀 Try it yourself

```bash
./0-select_states.py root root hbtn_0e_0_usa   # raw SQL: list the states
./10-model_state_my_get.py root root hbtn_0e_6_usa Texas
python3 -c "from model_state import State; print(State.__table__)"
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
