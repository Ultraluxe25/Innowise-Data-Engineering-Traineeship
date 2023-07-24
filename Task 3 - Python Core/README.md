# Task 1. Python introduction

This project is a Python application for managing data related to rooms and students. It provides functionalities to read data from JSON files, create and manage a PostgreSQL database, and execute database queries.

## Installation
To run this project, you need Python 3.x installed on your system. You can install the required Python packages using **pip** by running the following command:

```bash
pip install -r requirements.txt
```
Make sure to set up a PostgreSQL database and update the **config.json** file with your database credentials.

## Usage
### 1. Setup Database
1. Create a PostgreSQL database.
2. Update the **config.json** file with your database credentials.
### 2. Run the Application
To run the application, execute the **main.py** script:
```bash
python main.py
```

The script performs the following steps:

1. Connects to the PostgreSQL database using the provided credentials.
2. Reads data from JSON files (**rooms.json** and **students.json**) and stores it in DataFrames.
3. Creates tables **rooms** and **students** in the database.
4. Loads data from DataFrames into the corresponding database tables.
5. Executes database queries and saves the results in JSON and XML formats in the **exported results** folder.
### 3. Unit Tests
To run the unit tests, execute the **test_project.py** script:
```bash
python test_project.py
```
The unit tests verify the functionalities of the **JSONReader** and **DataBaseCreator** classes.

## Project Structure
The project has the following structure:

```graphql
├── main.py           # Main script to run the application
├── test_project.py   # Unit tests
├── config.json       # Configuration file with database credentials
├── requirements.txt  # Required Python packages
├── json_reader.py    # Module for reading data from JSON files
├── database_creator.py  # Module for creating and managing the PostgreSQL database
├── queries.py        # Contains SQL queries used in the application
├── export.py         # Module for executing queries and exporting results
├── test_data         # Folder containing test JSON data
│   ├── test_json.json  # Sample JSON data for unit tests
├── exported results  # Folder to store exported results (JSON and XML)
│   ├── json          # JSON files with query results
│   └── xml           # XML files with query results
```

## License
This project is licensed under the **MIT License.**

## Contributing
Pull requests and bug reports are welcome. For major changes, please open an issue first to discuss what you would like to change.
