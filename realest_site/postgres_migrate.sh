#!/bin/sh

if [ -n "$POSTGRES_FLUSH" ]; then
    python manage.py flush --no-input
fi

while ! nc -z $POSTGRES_HOST 5432; do
    echo "Waiting for postgres to start up properly..."
    sleep 0.5
done

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec "$@"
