### You can find Pagila's scheme at [postgresqltutorial.com](https://www.postgresqltutorial.com/postgresql-getting-started/postgresql-sample-database/)

### You can download files from Pagila's repository [here](https://github.com/devrimgunduz/pagila)

# To create and fill database in PostgreSQL do next steps:
1. Create new database **Pagila** in PgAdmin 4.
2. Switch on auto-commit mode in PgAdmin 4.
3. Download, copy, paste and run file **pagila-schema.sql** with PgAdmin 4 in query window to create schema.
4. Download, copy, paste and run file **pagila-insert-data.sql** with PgAdmin 4 in query window to insert values into database.


# To get database from Docker-Compose
1. Run Docker Desktop
2. Print in *cmd* at folder where you store *.yml* file ```bash docker-compose up```.
3. At Docker push 'Open in Browser' pgadmin4_c in container section.
4. Sign in using current info:
    PGADMIN_DEFAULT_EMAIL: admin@admin.com
    PGADMIN_DEFAULT_PASSWORD: root
