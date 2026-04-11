<div align="center">

# 🗄️ SQL — introduction

**CREATE, SELECT, INSERT — your first database, straight from the terminal.**

[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com)
[![SQL](https://img.shields.io/badge/SQL-DDL%20%C2%B7%20DML-005C84?style=flat-square)](#)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

The first date with a database. Every task is a `.sql` file executed
against a local MySQL server: creating databases and tables only when they
don't exist, `DESCRIBE`-ing structure, `SELECT`-ing, `INSERT`-ing,
`UPDATE`-ing — and gradually meeting `AVG()`, `GROUP BY`, `SUM()` and
sorting on computed columns.

The data is a school: students with scores and birth states. By the last
tasks the queries answer real questions — *what's the average temperature
per city, which state was born first* — with one-line SQL that would take
a paragraph of code.

## 🎯 Concepts covered

- `CREATE DATABASE` / `CREATE TABLE IF NOT EXISTS`
- `SHOW` databases & tables, `DESCRIBE`
- `SELECT` — columns, `WHERE`, `ORDER BY`
- `INSERT INTO` — single rows and multi-row
- `UPDATE … SET … WHERE` — and why the WHERE matters
- Aggregates: `AVG()`, `SUM()`, `MAX()`, `GROUP BY`
- Comments with `--` and batch mode (`mysql < file.sql`)

## 📂 Files

| File | What it does |
|---|---|
| [`0-list_databases.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/0-list_databases.sql) | `SHOW DATABASES` — the opening move |
| [`1-create_database_if_missing.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/1-create_database_if_missing.sql) | Creates the database — only if it isn't there |
| [`10-top_score.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/10-top_score.sql) | Best score, sorted descending |
| [`100-move_to_utf8.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/100-move_to_utf8.sql) | Converts the database & table to `utf8mb4` |
| [`101-avg_temperatures.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/101-avg_temperatures.sql) | Average temperature per city, descending |
| [`102-top_city.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/102-top_city.sql) | The city with the highest average temperature |
| [`103-max_state.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/103-max_state.sql) | The state with the earliest birth date |
| [`11-best_score.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/11-best_score.sql) | Scores above a threshold |
| [`12-no_cheating.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/12-no_cheating.sql) | `UPDATE` — correcting a grade |
| [`13-change_class.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/13-change_class.sql) | `UPDATE` on a specific record |
| [`14-average.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/14-average.sql) | `AVG()` — the class average |
| [`15-groups.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/15-groups.sql) | `GROUP BY` — counting per group |
| [`16-no_link.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/16-no_link.sql) | `WHERE` a column isn't NULL |
| [`2-remove_database.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/2-remove_database.sql) | Drops a database in MySQL land… |
| [`3-list_tables.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/3-list_tables.sql) | `SHOW TABLES` of a database |
| [`4-first_table.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/4-first_table.sql) | Creates the first table: `id`, `name` |
| [`5-full_table.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/5-full_table.sql) | `DESCRIBE` — the table's anatomy |
| [`6-list_values.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/6-list_values.sql) | The first `SELECT * FROM` |
| [`7-insert_value.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/7-insert_value.sql) | Adds a row to the table |
| [`8-count_89.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/8-count_89.sql) | Counts records — the first aggregate |
| [`9-full_creation.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_introduction/9-full_creation.sql) | A complete script: database + table + data |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · **MySQL 8.0** (username/password passed per task)
- 📄 All `.sql` files run in **batch mode**: `mysql -uuser -ppass < file.sql`
- ✍️ SQL comments start with `--` on its own line

## 🚀 Try it yourself

```bash
mysql -uroot -proot hbtn_0c_0 < 6-list_values.sql
mysql -uroot -proot hbtn_0c_0 < 14-average.sql   # AVG() with aliases
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
