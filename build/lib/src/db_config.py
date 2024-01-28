#src/db_config.py
def get_db_credentials():
    with open('db_credentials.txt', 'r') as f:
        dbname = f.readline().strip()
        user = f.readline().strip()
        password = f.readline().strip()
        host = f.readline().strip()
        port = f.readline().strip()
    return dbname, user, password, host, port