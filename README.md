# Realest Project

Demo web-crawling and backend project using scrapy framework and Django

## Deployment

The whole project can be deployed with `docker`. To set up all the components
you can simply run
```bash
docker compose up --build
```

The website will be available at the address `localhost:8080`.

The database storage is persisted across docker image runtimes using the
volume `postgres_data`. In order to clear the database run the compose
command with the environment variable `POSTGRES_FLUSH=1`:
```bash
POSTGRES_FLUSH=1 docker compose up --build
```
