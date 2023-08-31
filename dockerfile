# Use a base image with Python and PyQt6 pre-installed
FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Install PyQt6
RUN pip install PyQt6

# Copy your application files into the container
COPY . /app

# Command to run your PyQt6 application
CMD ["python", "main.py"]
