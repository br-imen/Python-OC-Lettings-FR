#!/bin/sh

# Check if the environment is not production
if [ "$ENVIRONMENT" != "production" ]; then
  # Check if the .env file exists and copy it if it does
  if [ -f /app/.env ]; then
    cp /app/.env /etc/secrets/.env
  fi
fi


# If the environment is production, run collectstatic
if [ "$ENVIRONMENT" = "production" ]; then
  echo "Running migrate..."
  python manage.py migrate --noinput
  echo "Running collecttatic..."
  python manage.py collectstatic --noinput
fi

# Then start the application
exec "$@"