import os
import json
import logging
from datetime import timedelta
import psycopg2
import xml.etree.ElementTree as ET


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class Exporter:
    def __init__(self, config_file):
        with open(config_file) as config_file:
            config = json.load(config_file)

        self.dbname = config["dbname"]
        self.user = config["user"]
        self.password = config["password"]
        self.host = config["host"]
        self.port = config["port"]
        self.connection = None


    def connect(self):
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


    def execute_query(self, query):
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
        try:
            if self.connection:
                self.connection.close()
                print('Disconnect DB')
        except (Exception, psycopg2.Error) as error:
            print('Error during disconnection:', error)
        finally:
            self.connection = None


    def save_as_json(self, data, file_name):
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


    def save_as_xml(self, data, file_name):
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
