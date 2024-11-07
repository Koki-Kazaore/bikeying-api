# Bikeying API

### Installing Dependant Packages
```bash
$ pipenv install --dev
```

### (Option) Add the package you need
```bash
$ pipenv install {package-A} {package-B} ...
```

### Launching the virtual environment
```bash
$ pipenv shell
```

### Server Startup
```bash
$ uvicorn main:app --reload

# To launch a specific file
$ uvicorn bikes.app:app --reload

# To launch with flask
$ flask run --reload
```

### Migration
To create a new migration script, run the following command `<message>` is a description of the migration.
```bash
$ PYTHONPATH='pwd' alembic revision --autogenerate -m "<message>"
```

To apply the migration to the database, execute the following command.
```bash
$ PYTHONPATH='pwd' alembic upgrade heads
```

To downgrade to a specific revision, run the following command where `<revision>` is the revision ID.
```bash
$ PYTHONPATH='pwd' alembic downgrade <revision>
```

### API　Documentation
- Redoc: `http://127.0.0.1:8000/redoc`
- Swagger: `http://127.0.0.1:8000/docs`