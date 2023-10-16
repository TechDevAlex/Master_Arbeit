import psycopg2

db_uri = 'postgresql://postgres:400840@localhost/sample_db'

conn = psycopg2.connect(db_uri)
cursor = conn.cursor()

cursor.execute("SELECT * FROM users;")
users = cursor.fetchall()
print(users)

cursor.close()
conn.close()
