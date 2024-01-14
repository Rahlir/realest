FROM python:3.11-alpine as requirements

ENV POETRY_VERSION=1.7.1 \
    POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME=/opt/poetry

RUN python3 -m venv $POETRY_HOME
RUN $POETRY_HOME/bin/pip install poetry==$POETRY_VERSION

WORKDIR /var/lib/realest_scrap

COPY poetry.lock pyproject.toml ./

RUN $POETRY_HOME/bin/poetry export -f requirements.txt --without-hashes -o requirements.txt


FROM python:3.11-alpine

RUN apk update && apk add curl

WORKDIR /opt/realest_scrap

COPY --from=requirements /var/lib/realest_scrap/requirements.txt ./
RUN apk add --no-cache postgresql-libs && \
    apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
    pip install -r requirements.txt && \
    apk --purge del .build-deps

COPY  . .

EXPOSE 6800

ENTRYPOINT ["./setup_scrapyd.sh"]

CMD ["scrapyd"]
