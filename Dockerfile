# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /

# Copy files to the working directory
COPY . .

# Upgrade pip and install the application dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Set the command to run your application
CMD [ "python", "main.py" ]