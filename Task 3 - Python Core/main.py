import json
import logging
import json_reader
import database_creator
import queries
import export


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def load_config() -> dict:
    '''
    Loads the configuration from the "config.json" file.

    Returns:
    dict: A dictionary containing the configuration data.
    '''
    with open('config.json') as config_file:
        return json.load(config_file)


def main() -> None:
    '''
    The main function that orchestrates the data loading, database creation, query execution, and exporting.

    This function reads data from JSON files, connects to the database, creates tables, inserts data, executes queries,
    and exports the results in JSON and XML formats.
    '''
    config = load_config()

    # Connect to DB:
    print('Connecting to Your database...')

    dbname = config["dbname"]
    user = config["user"]
    password = config["password"]
    host = config["host"]
    port = config["port"]

    # Create a database connector and connect to the database
    db_connector = database_creator.DataBaseCreator("config.json")
    db_connector.connect()

    # Add data from json to pandas DataFrame
    rooms = json_reader.JSONReader('initial data/json/rooms.json').read_json()
    students = json_reader.JSONReader('initial data/json/students.json').read_json()

    # Create rooms and students tables
    db_connector.create_table_rooms()
    db_connector.create_table_students()

    # Insert data into rooms and students tables
    db_connector.load_data_to_rooms_table(rooms)
    db_connector.load_data_to_students_table(students)

    # Disconnect from the database
    db_connector.disconnect()

    # Create a database extractor and connect to the database
    db_extractor = export.Exporter("config.json")
    db_extractor.connect()

    # Execute queries and save results in JSON and XML formats
    results1 = db_extractor.execute_query(queries.query1)
    db_extractor.save_as_json(results1, 'query1_results')
    db_extractor.save_as_xml(results1, 'query1_results')

    results2 = db_extractor.execute_query(queries.query2)
    db_extractor.save_as_json(results2, 'query2_results')
    db_extractor.save_as_xml(results2, 'query2_results')

    results3 = db_extractor.execute_query(queries.query3)
    db_extractor.save_as_json(results3, 'query3_results')
    db_extractor.save_as_xml(results3, 'query3_results')

    results4 = db_extractor.execute_query(queries.query4)
    db_extractor.save_as_json(results4, 'query4_results')
    db_extractor.save_as_xml(results4, 'query4_results')

    # Disconnect from the database
    db_extractor.disconnect()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)  # Basic configuration for logging
    main()
