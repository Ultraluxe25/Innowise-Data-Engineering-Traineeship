import json_reader
import database_connector


class RoomsTableCreator(database_connector.DBConnector):
    '''
    Inherited сlass create table room for db
    '''
    pass    


class StudentsTableCreator(database_connector.DBConnector):
    '''
    Inherited сlass create table room for db
    '''
    pass


# Connect to DB:
print('Connecting to Your database...')
secret = input('Type your password: ')
connector = database_connector.DBConnector(
    dbname='postgres',
    user='postgres',
    password=secret,
    host='localhost',
    port='5432',
)
connector.connect()

# Add data from json to pandas DataFrame
rooms = json_reader.JSONReader('json/rooms.json').read_json()
students = json_reader.JSONReader('json/students.json').read_json()

# Create rooms and students tables
connector.create_table_rooms()
connector.create_table_students()

# Insert data into rooms and students tables
connector.load_data_to_rooms_table(rooms)
connector.load_data_to_students_table(students)

# Disconnect from the database
connector.disconnect()
