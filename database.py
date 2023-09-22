import psycopg2

def connect_to_database():
    try:
        connection = psycopg2.connect(
            host="localhost",
            database="dvdrental",
            user="postgres",
            password="EnterYourPasswordHere"
        )
        print("Connected to PostgreSQL")
        return connection
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL:", error)
        return None
def close_connection(connection):
    try:
        if connection:
            connection.close()
            print("PostgreSQL connection is closed")
    except Exception as error:
        print("Error while closing PostgreSQL connection:", error)

def execute_query(connection, query):
    try:
        cursor = connection.cursor()
        cursor.execute(query)
        return cursor
    except Exception as error:
        print("Error while executing query:", error)
        return None

# Other of your database functions

if __name__ == "__main__":
    connection = connect_to_database()
    if connection:
        # Perform any database operations or testing here
        # For example, you can execute a query to check the database connection:
        cursor = connection.cursor()
        cursor.execute("SELECT version();")
        record = cursor.fetchone()
        print("You are connected to -", record[0])

    # Close the connection when you're done
    if connection:
        connection.close()
        print("PostgreSQL connection is closed")
