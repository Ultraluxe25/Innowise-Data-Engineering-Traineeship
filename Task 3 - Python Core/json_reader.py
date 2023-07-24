import json
import logging
import pandas as pd


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class JSONReader:
    '''
    Class to read data from JSON files and convert it to a DataFrame.
    '''

    def __init__(self, file_name: str) -> None:
        '''
        Constructor for the JSONReader class.

        Parameters:
        file_name (str): The path to the JSON file to be read.
        '''
        self.file_name = file_name

    def read_json(self) -> pd.DataFrame:
        '''
        Reads data from the JSON file and converts it to a DataFrame.

        Returns:
        pd.DataFrame: A DataFrame containing the data from the JSON file.
        '''
        try:
            with open(self.file_name) as json_data:
                data = json.load(json_data)
                df = pd.DataFrame(data)
            logger.info(f'Read data from JSON file: {self.file_name}')
            return df
        # json.JSONDecodeError is an error that occurs when decoding or parsing a JSON string
        # into a Python object. It indicates an invalid JSON data format.
        except (FileNotFoundError, json.JSONDecodeError) as error:
            logger.error(f'Error during reading json-file: {error}')
            print('Error during reading json-file:', error)
