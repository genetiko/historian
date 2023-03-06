# historian
Сбор, хранение и управление историческими данными


Run Postgres

```shell
docker run -d -p 5432:5432 -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=historian --name historian-db postgres
```


Create new revision

```shell
alembic revision -m "Add a column"
```

Run migrations

```shell
alembic upgrade head
```