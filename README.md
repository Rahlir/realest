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

## Architecture Notes

For the architecture, I have picked `scrapy` framework with deployment using [scrapyd](https://scrapyd.readthedocs.io/en/latest/overview.html)
in order to be able to send crawling requests using REST API. For the website, I have
picked `django` framework. For such a small application, [FastAPI](https://fastapi.tiangolo.com/) would probably be
more suitable. However, since it was necessary to also build a simple frontend, `django`
was more suitable since `FastAPI` can only build pure REST API and building a separate
JavaScript frontend would be an overkill.

Right now, no unit tests were written since the application is of a very small size. Nevertheless,
testing architecture is prepared in place: for `realest_scrap`, testing can be done with [pytest](https://docs.pytest.org/en/7.4.x/),
for `realest_site`, testing can be done with builtin test infrastructure of `django`.
