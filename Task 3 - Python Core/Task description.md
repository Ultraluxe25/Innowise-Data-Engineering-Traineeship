**Task Description:**

Using a MySQL (or another relational DB like PostgreSQL), create a database schema corresponding to the files provided in the attachment, establishing a many-to-one relationship.

Write a script with the aim of loading these two files and saving the data into the database.

The following queries will be required to be executed on the database:

1. List of rooms and the number of students in each room.
2. 5 rooms with the smallest average age of students.
3. 5 rooms with the largest age difference among students.
4. List of rooms where students of different genders live.

**Requirements and Notes:**

- Suggest optimizations for the queries using indexes.
- Generate an SQL query that adds the necessary indexes.
- Export the results in JSON or XML format.
- All mathematical calculations should be performed at the database level.
- Use object-oriented programming (OOP) and follow SOLID principles.
- Avoid using ORM (use raw SQL).

**Command Line Interface (CLI) Parameters:**

The script should support the following input parameters:

- `students` (path to the students file).
- `rooms` (path to the rooms file).
- `format` (output format: xml or json).

Before starting the task:

- Make sure you understand the requirements correctly.
- Set up and configure a virtual environment.
- Plan the architecture.
- Decompose the task into subtasks in a Jira ticket.
