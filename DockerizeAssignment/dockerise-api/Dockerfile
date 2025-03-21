# Use official Python image as a base
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the Flask app to the container
COPY app.py /app

COPY ./templates /app/templates

COPY ./requirements.txt /app/requirements.txt
# Install dependencies
RUN pip install -r /app/requirements.txt

# Expose the Flask app's port
EXPOSE 3000

# Run the Flask app
CMD ["python", "app.py"]

