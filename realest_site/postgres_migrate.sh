#!/bin/sh

if [ -n "$POSTGRES_FLUSH" ]; then
    python manage.py flush --no-input
fi

python manage.py migrate

exec "$@"
