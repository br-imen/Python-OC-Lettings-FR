# Use the official Python image as the base image
FROM python:3.11-slim

# Install bash
RUN apt-get update && apt-get install -y bash

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the container
COPY requirements.txt /app/

# Install any dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire Django project to the container
COPY . /app/
COPY .env /app/.env


# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the Django development server
CMD ["bash", "-c", "source /app/.env && python manage.py runserver 0.0.0.0:8000"]

