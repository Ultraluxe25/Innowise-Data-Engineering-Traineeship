# Task 1. Python introduction

The project is a part of data engineering internship and represents the implementation of ETL process. Data extraction comes from JSON files, transformation with pandas and loading into PostgreSQL. 

The following topics were covered when creating the project:

* Logging in Python
* Python Testing With Pytest
* Docker and docker compose
* Managing PostgreSQL with Python
* Build Command-Line Interfaces With Python's argparse
* Linting & Formatting
* Git pre commit hooks


## Files and modules and What They Do

| Name | Description |
| - | - |
| [`main.py`](/main.py) | A Python script to start ETL process and load data to PostgreSQL database  |
| [`cli.py`](/cli.py) | Python CLI script that provides data extract functionality from a PostgreSQL database using --students "path/to/file" --rooms "path/to/file" --format [json / xml] |
| [`modules/`](/modules/) | module contains main classes and sql queries |
| [`modules/db/`](/modules/db/) | module contains class for db operations and corresponding config |
| [`modules/logs/`](/modules/logs/) | module contains customized logger and corresponding config |
| [`modules/scripts/`](/modules/scripts/) | module contains class of main ETL process |
| [`modules/sql/`](/modules/sql/) | module contains sql queries to PostgreSQL database |
| [`init-multi-postgres-databases.sh`](/init-multi-postgres-databases.sh) | init script to create production and test postgreSQL databases in one container |

## Getting Started
### Prerequisites

* python >= 3.8.10
* Docker 20.10.23
* docker-compose 2.15.1

### Installation

1. Clone the repo 
```sh 
git clone git@github.com:monometa/innowise_task1_python_intro.git
```
2. Set environment variables
```sh 
mv env-example.txt .env
```
3. Build and run docker-compose
```sh
run docker-compose up -d --build
```

## SQL queries

Список комнат и количество студентов в каждой из них

```sql
select rooms.name, count(rooms.id)
from rooms
         left join students on rooms.id = students.room
group by rooms.id;
```

5 комнат, где самый маленький средний возраст студентов

```sql
select
  rooms.id,
  rooms.name,
  avg(age(current_date, birthday))
from
  rooms
  inner join students on rooms.id = students.room
group by
  rooms.id
order by
  avg(age(current_date, birthday)) asc
limit
  5;
```
5 комнат с самой большой разницей в возрасте студентов

```sql
select
  rooms.name
from
  rooms
  inner join students on rooms.id = students.room
group by
  rooms.id
order by
  max(birthday) - min(birthday) desc
limit
  5;
```

Список комнат где живут разнополые студенты
```sql
select
  id
from
  (
    select
      rooms.id,
      students.sex
    from
      rooms
      inner join students on rooms.id = students.room
    group by
      rooms.id,
      students.sex
  ) temp
group by
  id
having
  count(id) = 2;
```