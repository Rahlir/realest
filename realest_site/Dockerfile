FROM python:3.11-alpine as requirements

ENV POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/opt/poetry

RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION

WORKDIR /var/lib/realest_site

COPY poetry.lock pyproject.toml ./

RUN $POETRY_HOME/bin/poetry export -f requirements.txt --without-hashes -o requirements.txt


FROM python:3.11-alpine

WORKDIR /opt/realest_site

COPY --from=requirements /var/lib/realest_site/requirements.txt ./

RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps

RUN apk add --no-cache netcat-openbsd

COPY  . .

EXPOSE 8000

ENTRYPOINT ["./postgres_migrate.sh"]

CMD ["gunicorn", "realest_site.wsgi:application", "--bind", "0.0.0.0:8000"]
