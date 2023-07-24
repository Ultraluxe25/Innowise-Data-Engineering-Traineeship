import json
import logging
import psycopg2
import pandas as pd

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class DataBaseCreator:
    '''
    Class connects with PostgreSQL database and creates tables and loads data into them.
    '''

    def __init__(self, config_file: str):
        '''
        Constructor for the DataBaseCreator class.

        Parameters:
        config_file (str): The path to the JSON config file containing database connection details.
        '''
        with open(config_file) as config_file:
            config = json.load(config_file)

        self.dbname = config["dbname"]
        self.user = config["user"]
        self.password = config["password"]
        self.host = config["host"]
        self.port = config["port"]
        self.connection = None

    def connect(self):
        '''
        Function connects to PostgreSQL database.
        '''
        try:
            self.connection = psycopg2.connect(
                database=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
            )
            print('Successful connection!')
            logger.info('Successful connection to the database!')
        except (Exception, psycopg2.Error) as error:
            logger.error(f'Error during connection: {error}')
            print('Error during connection:', error)

    def create_table_rooms(self):
        '''
        Creates an empty table named "rooms".
        '''
        drop_table_rooms_query = '''
        DROP TABLE IF EXISTS rooms
        '''

        create_room_table_query = '''
        CREATE TABLE
            rooms (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50)
            )
        '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(drop_table_rooms_query)
            cursor.execute(create_room_table_query)
            self.connection.commit()
            print('Table Rooms created successfully!')
        except (Exception, psycopg2.Error) as error:
            print('Error during table rooms creation:', error)

    def create_table_students(self):
        '''
        Creates an empty table named "students".
        '''
        drop_table_students_query = '''
        DROP TABLE IF EXISTS students
        '''

        create_students_table_query = '''
        CREATE TABLE
            students (
                id SERIAL PRIMARY KEY,
                birthday DATE,
                name VARCHAR(100),
                room INTEGER,
                sex CHAR(1)
            )
        '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(drop_table_students_query)
            cursor.execute(create_students_table_query)
            self.connection.commit()
            print('Table Students created successfully!')
        except (Exception, psycopg2.Error) as error:
            print('Error during table students creation:', error)

    def load_data_to_rooms_table(self, df: pd.DataFrame):
        '''
        Loads data from a DataFrame to the "rooms" table.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data to be loaded.
        '''
        try:
            cursor = self.connection.cursor()
            for _, row in df.iterrows():
                name = row['name']
                insert_query = f"INSERT INTO rooms (name) VALUES ('{name}')"
                cursor.execute(insert_query)
            self.connection.commit()
            print('Data loaded to "rooms" table successfully!')
        except (Exception, psycopg2.Error) as error:
            print('Error during data loading to "rooms" table:', error)

    def load_data_to_students_table(self, df: pd.DataFrame):
        '''
        Loads data from a DataFrame to the "students" table.

        Parameters:
        df (pd.DataFrame): The DataFrame containing the data to be loaded.
        '''
        try:
            cursor = self.connection.cursor()
            for _, row in df.iterrows():
                birthday = row['birthday']
                name = row['name']
                room = row['room']
                sex = row['sex']
                insert_query = f"INSERT INTO students (birthday, name, room, sex) VALUES ('{birthday}', '{name}', {room}, '{sex}')"
                cursor.execute(insert_query)
            self.connection.commit()
            print('Data loaded to "students" table successfully!')
        except (Exception, psycopg2.Error) as error:
            print('Error during data loading to "students" table:', error)

    def disconnect(self):
        '''
        Disconnects from the PostgreSQL database.
        '''
        try:
            if self.connection:
                self.connection.close()
                print('disconnect DB')
        except (Exception, psycopg2.Error) as error:
            print('Error during disconnection:', error)
        finally:
            self.connection = None
