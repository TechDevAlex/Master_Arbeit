from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
import os
import psycopg2

app = Flask("SustainableMaterialsApp")

# Replace with your PostgreSQL database URI without specifying the database name
db_uri = 'postgresql://postgres:400840@localhost/'

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)

# Define the User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Function to load data from a SQL file
def load_data_from_sql_file(filename):
    with open(filename, 'r') as file:
        sql_commands = file.read().split(';')

    for command in sql_commands:
        if command.strip():
            db.session.execute(text(command))



# Calculate the relative path to sample_data.sql in the same folder
current_dir = os.path.dirname(os.path.abspath(__file__))
sample_data_file = os.path.join(current_dir, 'sample_data.sql')

with app.app_context():
    # No need to create the database here as it has already been created
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri + 'sample_db'
    db.create_all()

    # Load data into the database
    load_data_from_sql_file(sample_data_file)
    db.session.commit()


#rerouting to the various templates

@app.route('/users')
def users():
    # You can add logic here to retrieve data from the database and pass it to the template
    # For now, let's assume a list of sample users
    sample_users = ["User1", "User2", "User3"]
    
    return render_template('users.html', users=sample_users)

@app.route('/')
def welcome():
    return render_template('welcome.html')


if __name__ == '__main__':
    app.run()



if __name__ == '__main__':
    app.run()
