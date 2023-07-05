# Use an official Python runtime as the base image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the application dependencies
RUN python -m venv venv
RUN . venv/bin/activate

# Upgrade pip and install the application dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY . .

# Set the command to run your application
CMD [ "python", "main.py" ]