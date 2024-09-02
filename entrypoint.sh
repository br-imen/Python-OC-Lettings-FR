#!/bin/sh

# If the environment is production, run collectstatic
if [ "$ENVIRONMENT" = "production" ]; then
  echo "Running migrate..."
  python manage.py migrate --noinput
  echo "Running collecttatic..."
  python manage.py collectstatic --noinput
fi

# Then start the application
exec "$@"