FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt /app

# Install Django
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . /app/

# Expose a port (e.g., 8000) that your application will run on
EXPOSE 8000


