# Realest Project

Realest real estate demo web-crawling (of the Czech website _sreality.cz_) and
backend project using the [Scrapy](https://scrapy.org/) and [Django](https://www.djangoproject.com/).

## Deployment

The whole project can be deployed with `docker`. To set up all the components
you can simply run
```bash
docker compose up --build
```

The website will then be available at the address `localhost:8080`.

The database storage is persisted across docker image runtimes using the
volume `postgres_data`. In order to flush the Django database, run the compose
command with the environment variable `POSTGRES_FLUSH=1`:
```bash
POSTGRES_FLUSH=1 docker compose up --build
```

Note that this will **not** clear the real estate entries from the database
collected by the crawler.

In order to completely wipe the databse, you need to remove the corresponding
docker volume:
```bash
docker volume rm realest_postgres_data
```

## Usage

The "frontend" is fairly self-intuitive. You can request crawl of `sreality.cz` through
the web form and then browse the scraped postings. The postings can also be viewed
in a detail view using the links in the list view.
