# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Upgrade pip and install the application dependencies
RUN pip install --no-cache-dir --upgrade pip

# Set the working directory inside the container
WORKDIR /app/

# Install dependencies
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy files to the working directory
COPY . .

# Set the command to run your application
CMD [ "python", "/app/main.py" ]