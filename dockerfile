# Use an official Python runtime as the base image
FROM python:3.9

# Install PyQt6 and required OpenGL libraries
RUN apt-get update && \
    apt-get install -y libgl1-mesa-glx && \
    pip install --no-cache-dir PyQt6

# Set the working directory in the container
WORKDIR /app

# Copy the application code into the container at /app
COPY app.py /app/

# Command to run the application
CMD ["python", "app.py"]
