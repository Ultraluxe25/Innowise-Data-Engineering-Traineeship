import os
import json
import logging
from datetime import timedelta
import psycopg2
import xml.etree.ElementTree as ET


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Exporter:
    '''
    Class to export data to JSON and XML formats.
    '''

    def __init__(self, config_file: str):
        '''
        Constructor for the Exporter class.

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
        except (Exception, psycopg2.Error) as error:
            print('Error during connection:', error)

    def execute_query(self, query: str) -> list:
        '''
        Executes the provided SQL query and returns the results.

        Parameters:
        query (str): The SQL query to be executed.

        Returns:
        list: A list of tuples containing the results of the query.
        '''
        try:
            cursor = self.connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except (Exception, psycopg2.Error) as error:
            print('Error during query execution:', error)
            return None

    def disconnect(self):
        '''
        Disconnects from the PostgreSQL database.
        '''
        try:
            if self.connection:
                self.connection.close()
                print('Disconnect DB')
        except (Exception, psycopg2.Error) as error:
            print('Error during disconnection:', error)
        finally:
            self.connection = None

    def save_as_json(self, data: list, file_name: str):
        '''
        Saves the data as JSON format.

        Parameters:
        data (list): The data to be saved in JSON format (a list of tuples).
        file_name (str): The name of the file to be saved (without the file extension).
        '''
        def convert_timedelta_to_str(value):
            if isinstance(value, timedelta):
                return str(value.total_seconds())
            return value

        converted_data = [[convert_timedelta_to_str(val) for val in row] for row in data]

        # Create the 'exported_results' folder if it doesn't exist
        if not os.path.exists('exported results'):
            os.makedirs('exported results')

        # Create the 'json' subfolder if it doesn't exist
        if not os.path.exists(os.path.join('exported results', 'json')):
            os.makedirs(os.path.join('exported results', 'json'))

        with open(os.path.join('exported results', 'json', file_name + '.json'), 'w') as json_file:
            json.dump(converted_data, json_file)
        print(f'Results saved as exported results/json/{file_name}.json successfully!')
        logger.info(f'Results saved as exported results/json/{file_name}.json successfully!')

    def save_as_xml(self, data: list, file_name: str):
        '''
        Saves the data as XML format.

        Parameters:
        data (list): The data to be saved in XML format (a list of tuples).
        file_name (str): The name of the file to be saved (without the file extension).
        '''
        root = ET.Element('results')
        for row in data:
            room_number = row[0]  # Unpacking modified as we have only one value in the result
            room_element = ET.SubElement(root, 'room')
            room_element.set('number', str(room_number))

        # Create the 'exported_results' and 'xml' folders if they don't exist
        if not os.path.exists('exported results/xml'):
            os.makedirs('exported results/xml')

        tree = ET.ElementTree(root)
        tree.write(os.path.join('exported results', 'xml', file_name + '.xml'), encoding='utf-8', xml_declaration=True)
        print(f'Results saved as exported results/xml/{file_name}.xml successfully!')
        logger.info(f'Results saved as exported results/xml/{file_name}.xml successfully!')
