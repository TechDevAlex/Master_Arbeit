from gui.database import connect_to_database

def add_data_to_table(table_name, data):
    db_connection = connect_to_database()
    if db_connection:
        cursor = db_connection.cursor()
        columns = ', '.join([f"column_{i+1}" for i in range(len(data))])
        placeholders = ', '.join(['%s' for _ in data])
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        cursor.execute(insert_query, data)
        db_connection.commit()
        cursor.close()
