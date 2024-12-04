# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy only requirements.txt first to leverage caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app/

# Expose the port your application will run on
EXPOSE 8080

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
