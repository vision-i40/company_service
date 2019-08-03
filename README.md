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

Create a token for you to use.
```
    curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"email": "<USER_EMAIL_YOU_JUST_CREATED>", "password": "<PASSWORD_YOU_JUST_CREATE>"}' \
    http://localhost:8000/auth/token/

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
