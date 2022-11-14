# Desafio fullstack FPF Tech

## Backend

- FastApi (Python)
- Docker
- Postgres

## Frontend

- Angular
- Docker
- Angular Material
- Tailwind
- Nginx

## Execute

clone this repository and:

```bash
cd desafio-fpf
```

Copy the `.env.example` to `.env`. You can define other variables if you want.
In the `.env.example` the `POSTGRES_SERVER` refers to the db host, use "localhost" for a local instance (or container) or use "db" for docker-compose.

```bash
cat .env.example > .env
```

### with docker

here it is a little more complicated to understand if there is no basic knowledge of docker, but it works :).

```bash
docker-compose up api && docker-compose rm -fvs
```

In another terminal:

```bash
docker exec -it api sh

alembic upgrade head

exit
```

```bash
# OUTPUT
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> e2a16a925892, create product table
```

Now, tricky part here :), in `docker-compose.yml` uncomment this line:

```yml
api:
    ...
    command: bash -c "while true; do sleep 1; done"
    # command: "uvicorn src.main:app --host 0.0.0.0 --reload" <--- this line
```

```yml
api:
    ...
    # command: bash -c "while true; do sleep 1; done
    command: "uvicorn src.main:app --host 0.0.0.0 --reload"
```

```bash
docker-compose up && docker-compose rm -fvs
```

This start the services in:

| service | Tecnology |                    URL                    |
| ------- | :-------: | :---------------------------------------: |
| web     |  Angular  |      [clique aqui](http://localhost)      |
| api     |  Fastapi  | [clique aqui](http://localhost:8000/docs) |
| db      | Postgres  |          you can use a db client          |

### without docker

Setup the db variables in `.env`, the app use a [postgres database](https://www.postgresql.org/). You can create a Postgres container by setting the same environment variables in the `.env` that will also work.

#### start the backend

```bash
cd api

# venv recommended
pip install -r requirements.txt

alembic upgrade head

uvicorn src.main:app --reload
```

Alembic is used for migrations, you can view the sql in [migration](https://github.com/willidert/desafio-fpf/api/migration.sql) da raiz.

#### start the frontend

```bash
cd web

npm i
```

You can run with `npm run start` or `ng serve`.

This start the services in:

| service | Tecnology |                    URL                    |
| ------- | :-------: | :---------------------------------------: |
| web     |  Angular  |   [clique aqui](http://localhost:4200)    |
| api     |  Fastapi  | [clique aqui](http://localhost:8000/docs) |

## TODO

- [x] create angular project
- [x] create all api endpoints
- [x] add dockerfiles and compose
- [x] include instructions for execute
- [ ] deploy for prodution env
- [x] CI/CD configuration
- [x] Some tests
