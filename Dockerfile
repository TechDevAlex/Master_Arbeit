# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app


# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Expose the Flask app's port
EXPOSE 5000

# Change working directory to correctly run the flask app
WORKDIR /app/scripts/flask_app

# Run app.py when the container launches
CMD ["python","app.py" , "-h 0.0.0.0 -p 5000"]

#"scripts/flask_app/app.py"