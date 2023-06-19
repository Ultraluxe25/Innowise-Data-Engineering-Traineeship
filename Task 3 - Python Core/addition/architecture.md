## Database Architecture

### Table "rooms"

This table will store data about rooms. Each room will have a unique identifier (`id`) and a name (`name`).

The structure of the "rooms" table looks as follows:

| Field | Data Type   | Constraints |
|-------|-------------|-------------|
| id    | INTEGER     | PRIMARY KEY |
| name  | VARCHAR(50) | NOT NULL    |

### Table "students"

This table will store data about students. Each student will have a unique identifier (`id`), a name (`name`), a date of birth (`birthday`), a room number (`room_id`), and a gender (`sex`).

The structure of the "students" table looks as follows:

| Field     | Data Type    | Constraints   |
|-----------|--------------|---------------|
| id        | INTEGER      | PRIMARY KEY   |
| name      | VARCHAR(100) | NOT NULL      |
| birthday  | DATE         | NOT NULL      |
| room_id   | INTEGER      | FOREIGN KEY   |
| sex       | CHAR(1)      | NOT NULL      |

Note: The `room_id` field is a foreign key that references the `id` field of the "rooms" table. This establishes a many-to-one relationship between the "students" and "rooms" tables.

Therefore, the above-mentioned database architecture creates two tables: "rooms" and "students". The "rooms" table contains information about rooms, while the "students" table stores data about students, including the room they reside in. The relationship between the "students" and "rooms" tables is established using the foreign key "room_id", which references the room identifier in the "rooms" table.

This database architecture provides structured data storage and enables efficient execution of queries and operations on the data.