# Use the official Python image as the base image
FROM python:3.11-slim

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

# Accept build arguments and set them as environment variables
ARG SENTRY_DSN
ARG SECRET_KEY
ARG DEBUG
ARG ALLOWED_HOSTS

ENV SENTRY_DSN=$SENTRY_DSN
ENV SECRET_KEY=$SECRET_KEY
ENV DEBUG=$DEBUG
ENV ALLOWED_HOSTS=$ALLOWED_HOSTS

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application using Gunicorn
CMD exec gunicorn --bind "0.0.0.0:$PORT" oc_lettings_site.wsgi:application
