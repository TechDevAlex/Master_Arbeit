import psycopg2

# Replace these values with your database credentials
DB_NAME = "UserCredentials"
DB_USER = "testuser"
DB_PASSWORD = "12345"
DB_HOST = "localhost"  # When connecting from outside Docker, use localhost

# Establish a connection to the database
try:
    connection = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )

    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT version();")
    db_version = cursor.fetchone()
    print(f"Connected to {db_version}")

    # Close the cursor and connection
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error connecting to the database:", e)
