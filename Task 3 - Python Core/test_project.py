import unittest
import pandas as pd
import json_reader
import database_creator
import export

class TestJSONReader(unittest.TestCase):
    def test_read_json(self) -> None:
        '''
        Test reading JSON data and converting it to a DataFrame.
        '''
        # Sample JSON data for testing
        json_data = '[{"name": "Alice", "age": 25}, {"name": "Bob", "age": 30}, {"name": "Carol", "age": 22}]'
        with open('initial data/json/students.json', 'w') as file:
            file.write(json_data)

        json_reader_obj = json_reader.JSONReader('initial data/json/students.json')
        df: pd.DataFrame = json_reader_obj.read_json()

        # Test DataFrame attributes and values
        self.assertIsNotNone(df)
        self.assertEqual(df.shape, (3, 2))
        self.assertEqual(df.columns.tolist(), ['name', 'age'])
        self.assertEqual(df.loc[0, 'name'], 'Alice')
        self.assertEqual(df.loc[1, 'age'], 30)

class TestDataBaseCreator(unittest.TestCase):
    def test_create_and_load_tables(self) -> None:
        '''
        Test creating tables and loading data into them.
        '''
        # Sample data for testing
        rooms_data = [
            {'name': 'Room A'},
            {'name': 'Room B'},
            {'name': 'Room C'}
        ]
        students_data = [
            {'birthday': '1995-01-01', 'name': 'Alice', 'room': 1, 'sex': 'F'},
            {'birthday': '1996-02-02', 'name': 'Bob', 'room': 2, 'sex': 'M'},
            {'birthday': '1997-03-03', 'name': 'Carol', 'room': 3, 'sex': 'F'}
        ]
        rooms_df: pd.DataFrame = pd.DataFrame(rooms_data)
        students_df: pd.DataFrame = pd.DataFrame(students_data)

        # Create a database connector and connect to the database
        db_connector = database_creator.DataBaseCreator('config.json')
        db_connector.connect()

        # Test create tables
        db_connector.create_table_rooms()
        db_connector.create_table_students()

        # Test load data to tables
        db_connector.load_data_to_rooms_table(rooms_df)
        db_connector.load_data_to_students_table(students_df)

        # Fetch data from tables
        rooms_query: str = "SELECT * FROM rooms"
        students_query: str = "SELECT * FROM students"

        # Create a database extractor and connect to the database
        db_extractor = export.Exporter("config.json")
        db_extractor.connect()

        rooms_results: list = db_extractor.execute_query(rooms_query)
        students_results: list = db_extractor.execute_query(students_query)

        # Disconnect from the database
        db_connector.disconnect()
        db_extractor.disconnect()

        # Test if the tables were created and data was loaded correctly
        self.assertEqual(len(rooms_results), len(rooms_data))
        self.assertEqual(len(students_results), len(students_data))
        self.assertEqual(rooms_results[0][1], 'Room A')
        self.assertEqual(students_results[1][2], 'Bob')

if __name__ == '__main__':
    unittest.main()
