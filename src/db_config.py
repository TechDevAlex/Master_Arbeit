#src/db_config.py
import os

def get_db_credentials():
    # directory of the current script
    script_dir = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to the db_credentials.txt file in the src directory
    credentials_path = os.path.join(script_dir, 'db_credentials.txt')

    credentials = {}
    with open(credentials_path, 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            credentials[key] = value
    return credentials['dbname'], credentials['user'], credentials['password'], credentials['host'], credentials['port']