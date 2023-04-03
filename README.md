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


### Metadata service API:

split_period_into_chunks(instrument_id, instrument_type_id, start_date, end_date)
возвращает список [(start_date, end_date), ...], по сути это длинный период, разбитый на маленькие кусочки, максимально возможные для возврата данных

fetch_historical_data(instrument_id, instrument_type_id, date)
возвращает байтовый поток gziped данных, с форматом пока не совсем понятно, но я подумаю сегодня

fetch_sources
возвращает список возможных источников

fetch_source_meta(source_id)
возвращает метаинформацию по источнику данных + список айдишников поддерживаемых инструментов

fetch_instrument_meta(instrument_id)
возвращает метаинформацию по инструменту, в том числе со списком типов предоставляемых данных