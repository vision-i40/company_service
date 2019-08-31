# Company Service

### Dependencies

- Python 3.6
- Pipenv
- Pip
- Docker and Docker Compose

### Running

Copy the .env file from .env.example
```
    cp .env.example .env
```

User pipenv shell:
```
    pipenv shell
```

Run dependencies with docker-compose:
```
    docker-compose up -d
```

Run the migrations:
```
    python3 manage.py migrate
```

Run the application:
```
    python3 manage.py runserver
```

Create a super user
```
    python manage.py createsuperuser
```

### Running Tests

Run dependencies with docker-compose:
```
    docker-compose up -d
```

Run the migrations:
```
    python3 manage.py migrate
```

Run the tests:
```
    python3 manage.py test
```


### Documentation Reference

- [Authentication](https://github.com/vision-i40/company_service/tree/master/docs)
