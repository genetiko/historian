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

### Queries

```postgresql
with sub as (select job.import_job_id as id,
                    count(*)          as cnt
             from import_job_chunks job
             group by job.import_job_id)
select job.id,
       chunk.status,
       round(count(*) / (select sum(cnt) from sub where sub.id = job.id) * 100, 2) as percent
from import_jobs job
         inner join import_job_chunks chunk on job.id = chunk.import_job_id
group by job.id, chunk.status;



SELECT pg_size_pretty(pg_total_relation_size('mt5_rates'));

SELECT pg_size_pretty(pg_total_relation_size('mt5_ticks'));
```