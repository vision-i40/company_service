# Company Service

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
    python manage.py migrate
```

Run the application:
```
    python3 manage.py runserver
```

### Running Tests

Run dependencies with docker-compose:
```
    docker-compose up -d
```

Run the migrations:
```
    python manage.py migrate
```

Run the tests:
```
    python3 manage.py test
```