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
```

### API　Documentation
- Redoc: `http://127.0.0.1:8000/redoc`
- Swagger: `http://127.0.0.1:8000/docs`