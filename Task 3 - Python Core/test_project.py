import unittest
import pandas as pd
import json_reader


class TestJSONReader(unittest.TestCase):
    """
    Unit test for the JSONReader class.
    """
    def test_read_json(self) -> None:
        """
        Test reading JSON data and converting it to a DataFrame.
        """
        # Create a JSONReader instance for the test JSON file
        json_reader_instance: json_reader.JSONReader = json_reader.JSONReader('test_data/test_json.json')

        # Call the read_json() function to read the JSON data and get the DataFrame
        df: pd.DataFrame = json_reader_instance.read_json()

        # Assert that the DataFrame is not None
        self.assertIsNotNone(df)

        # Assert that the DataFrame is not empty
        self.assertGreater(len(df), 0)

        # Assert that the DataFrame has the expected shape (3 rows, 2 columns)
        self.assertEqual(df.shape, (3, 2))

        # Optionally, you can check the column names if needed
        expected_columns: list[str] = ['name', 'age']
        self.assertListEqual(list(df.columns), expected_columns)


if __name__ == '__main__':
    unittest.main()
