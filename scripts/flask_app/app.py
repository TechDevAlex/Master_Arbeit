from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text

app = Flask("sustainable_Materials_App")  

# Replace with your PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://testuser:12345@postgres-db/UserCredentials'
db = SQLAlchemy(app)

# Remove the User model

def load_data_from_sql_file(filename):
    with open(filename, 'r') as file:
        sql_commands = file.read().split(';')

    for command in sql_commands:
        if command.strip():
            db.session.execute(text(command))

# Function to insert a new user
def insert_user(username, password):
    insert_sql = "INSERT INTO users (username, password) VALUES (:username, :password)"
    db.session.execute(text(insert_sql), {"username": username, "password": password})
    db.session.commit()

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        insert_user(username, password)

    query = request.args.get('query')
    if query:
        query_sql = "SELECT username FROM users WHERE username = :username"
        result = db.session.execute(text(query_sql), {"username": query})
    else:
        query_sql = "SELECT username FROM users"
        result = db.session.execute(text(query_sql))

    users = [row[0] for row in result]
    return render_template('users.html', users=users)


@app.route('/')
def welcome():
    return render_template('welcome.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

