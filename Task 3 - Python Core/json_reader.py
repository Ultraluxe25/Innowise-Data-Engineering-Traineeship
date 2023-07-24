import json
import logging
import pandas as pd


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


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
            logger.info(f'Read data from JSON file: {self.file_name}')
            return df
        # json.JSONDecodeError is an error that occurs when decoding or parsing a JSON string
        # into a Python object. It indicates an invalid JSON data format.
        except (FileNotFoundError, json.JSONDecodeError) as error:
            logger.error(f'Error during reading json-file: {error}')
            print('Error during reading json-file:', error)
