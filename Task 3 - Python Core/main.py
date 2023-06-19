from __future__ import annotations

import json

import pandas as pd
import psycopg2


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

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
                print('disconnect DB')
        except (Exception, psycopg2.Error) as error:
            print('Error during disconnection:', error)
        finally:
            self.connection = None


# Connect to DB:
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

connector.disconnect()
