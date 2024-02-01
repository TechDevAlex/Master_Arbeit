#src\database\db_config.py
import os

def get_db_credentials():
    # Construct the path to the db_credentials.txt file relative to the project root directory
    credentials_path = os.path.join(os.path.dirname(os.getcwd()), 'Master_Arbeit','src', 'database', 'db_credentials.txt')

    credentials = {}
    with open(credentials_path, 'r') as f:
        for line in f:
            key, value = line.strip().split(' = ')
            credentials[key] = value
    return credentials['dbname'], credentials['user'], credentials['password'], credentials['host'], credentials['port']
