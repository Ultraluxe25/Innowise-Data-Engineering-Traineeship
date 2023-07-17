import json
import psycopg2
import pandas as pd


class JSONReader:
    '''
    Class reads data from json
    '''
    def __init__(self, file_name) -> None:
        self.file_name = file_name

    def read_json(self) -> pd.DataFrame:
        '''
        Function saves json-format data into DataFrame
        '''
        try:
            with open(self.file_name) as json_data:
                data = json.load(json_data)
                df = pd.DataFrame(data)
            return df
        # json.JSONDecodeError is an error that occurs when decoding or parsing a JSON string
        # into a Python object. It indicates an invalid JSON data format.
        except (FileNotFoundError, json.JSONDecodeError) as error:
            print('Error during reading json-file:', error)


class DBConnector:
    '''
    Class connects with PostgreSQL database
    '''
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None


    def connect(self):
        '''
        Function connects to PostgreSQL database
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
        # Exception is the base class for all exceptions in Python. psycopg2.
        # Error is an exception class defined in the psycopg2 library,
        # which is used to interact with a PostgreSQL database.
        except (Exception, psycopg2.Error) as error:
            print('Error during connection:', error)


    def create_table_rooms(self):
        '''
        Creates empty table
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
        except(Exception, psycopg2.Error) as error:
            print('Error during table rooms creation:', error)


    def create_table_students(self):
        '''
        Creates empty table
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
        except(Exception, psycopg2.Error) as error:
            print('Error during table students creation:', error)


    def load_data_to_rooms_table(self, df):
        '''
        Loads data from DataFrame to the "rooms" table
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


    def load_data_to_students_table(self, df):
        '''
        Loads data from DataFrame to the "students" table
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
        try:
            if self.connection:
                self.connection.close()
                print('disconnect DB')
        except (Exception, psycopg2.Error) as error:
            print('Error during disconnection:', error)
        finally:
            self.connection = None


class RoomsTableCreator(DBConnector):
    '''
    Inherited сlass create table room for db
    '''
    pass    


class StudentsTableCreator(DBConnector):
    '''
    Inherited сlass create table room for db
    '''
    pass


# Connect to DB:
print('Connecting to Your database...')
secret = input('Type your password: ')
connector = DBConnector(
    dbname='postgres',
    user='postgres',
    password=secret,
    host='localhost',
    port='5432',
)
connector.connect()

# Add data from json to pandas DataFrame
rooms = JSONReader('json/rooms.json').read_json()
students = JSONReader('json/students.json').read_json()

# Create rooms and students tables
connector.create_table_rooms()
connector.create_table_students()

# Insert data into rooms and students tables
connector.load_data_to_rooms_table(rooms)
connector.load_data_to_students_table(students)

# Disconnect from the database
connector.disconnect()
