<div align="center">

# 🔐 SQL — more queries

**JOINs, subqueries, user privileges — and a database full of shows.**

[![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=flat-square&logo=mysql&logoColor=white)](https://www.mysql.com)
[![SQL](https://img.shields.io/badge/SQL-DDL%20%C2%B7%20DML-005C84?style=flat-square)](#)
[![Holberton](https://img.shields.io/badge/Holberton-Foundations-E44D26?style=flat-square)](https://www.holbertonschool.com)

</div>

---

## 📖 About this project

Round two — the queries get relational. The dataset is a **streaming
service**: shows, genres, cast, ratings. `INNER JOIN`, `LEFT JOIN` and
`GROUP BY` combine to answer *which genres, which shows, which ratings* —
and subqueries appear where joins won't do.

The other half of the project is the part tutorials skip: **users and
privileges** — `CREATE USER`, `GRANT`, reading `SHOW GRANTS`, plus the
schema constraints that keep data honest: `NOT NULL`, `UNIQUE`, `DEFAULT`,
and `FOREIGN KEY`s between states and cities.

## 🎯 Concepts covered

- `INNER JOIN` / `LEFT JOIN` / `CROSS JOIN` — when each applies
- Subqueries as an alternative to joins
- `CREATE USER`, `GRANT`, `SHOW GRANTS`, `REVOKE`
- Constraints: `NOT NULL`, `UNIQUE`, `DEFAULT`
- `FOREIGN KEY` and referential integrity
- Aggregations over joined tables (`COUNT`, `GROUP BY`)

## 📂 Files

| File | What it does |
|---|---|
| [`0-privileges.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/0-privileges.sql) | `SHOW GRANTS` — who is allowed to do what |
| [`1-create_user.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/1-create_user.sql) | Creates a MySQL user, host by host |
| [`10-genre_id_by_show.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/10-genre_id_by_show.sql) | First JOIN on the TV database: genre per show |
| [`100-not_my_genres.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/100-not_my_genres.sql) | Genres that aren't in use |
| [`101-not_a_comedy.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/101-not_a_comedy.sql) | Everything that isn't a Comedy |
| [`102-rating_shows.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/102-rating_shows.sql) | Shows joined with their ratings |
| [`103-rating_genres.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/103-rating_genres.sql) | Average rating per genre |
| [`11-genre_id_all_shows.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/11-genre_id_all_shows.sql) | Every show's genre — or NULL (LEFT JOIN) |
| [`12-no_genre.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/12-no_genre.sql) | Shows with no genre listed |
| [`13-count_shows_by_genre.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/13-count_shows_by_genre.sql) | Show count per genre, grouped |
| [`14-my_genres.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/14-my_genres.sql) | All genres in the database, sorted |
| [`15-comedy_only.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/15-comedy_only.sql) | Just the comedies |
| [`16-shows_by_genre.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/16-shows_by_genre.sql) | Show titles grouped under each genre |
| [`2-create_read_user.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/2-create_read_user.sql) | A user with `SELECT`-only rights — least privilege |
| [`3-force_name.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/3-force_name.sql) | A table where `name` refuses to be NULL |
| [`4-never_empty.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/4-never_empty.sql) | `DEFAULT ''` — columns that are never empty |
| [`5-unique_id.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/5-unique_id.sql) | The `unique_id` column — 89 by default, never duplicated |
| [`6-states.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/6-states.sql) | Creates the `states` table |
| [`7-cities.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/7-cities.sql) | Creates `cities` with a `FOREIGN KEY` to states |
| [`8-cities_of_california_subquery.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/8-cities_of_california_subquery.sql) | California's cities — via subquery |
| [`9-cities_by_state_join.sql`](https://github.com/Abdullayews/holbertonschool-higher_level_programming/tree/main/SQL_more_queries/9-cities_by_state_join.sql) | The same result, the `JOIN` way |

## ⚙️ Requirements

- 🐧 Ubuntu 20.04 LTS · **MySQL 8.0**
- 📄 `.sql` files executed in batch mode: `mysql -uuser -ppass < file.sql`
- ✍️ SQL comments start with `--` on its own line

## 🚀 Try it yourself

```bash
mysql -uroot -p hbtn_0d_tvshows < 10-genre_id_by_show.sql
mysql -uroot -p hbtn_0d_tvshows < 16-shows_by_genre.sql   # JOIN + GROUP BY
```

---

✍️ **Muhəmməd Abdullayev** · [![GitHub](https://img.shields.io/badge/@Abdullayews-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/Abdullayews) · one of the projects in **[holbertonschool-higher_level_programming](../README.md)**
