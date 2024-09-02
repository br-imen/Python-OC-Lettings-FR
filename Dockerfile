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

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to use the script
ENTRYPOINT ["/app/entrypoint.sh"]

# Expose port 8000 to the outside world
EXPOSE 8000

# Command to run the application using Gunicorn
# CMD exec gunicorn --bind "0.0.0.0:8000" oc_lettings_site.wsgi:application
CMD python manage.py runserver 0.0.0.0:8000