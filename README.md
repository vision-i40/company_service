# Company Service

[![CircleCI](https://circleci.com/gh/vision-i40/company_service/tree/master.svg?style=svg)](https://circleci.com/gh/vision-i40/company_service/tree/master)

### Dependencies

- Python 3.6
- [Pip](https://linuxize.com/post/how-to-install-pip-on-ubuntu-18.04/)
- [Pipenv](https://docs.pipenv.org/en/latest/install/)
- Docker and Docker Compose

### Running

- Copy the .env file from .env.example
```
    cp .env.example .env
```
- Copy the local.py file from local.py.example
```
    cp company_service/settings/local.py.example company_service/settings/local.py
```
- Copy the test.py file from test.py.example
```
    cp company_service/settings/local.py.example company_service/settings/test.py
```
- User pipenv shell:
```
    pipenv shell
```

- Install all dependencies:
```
    pipenv install --dev
```

- Run dependencies with docker-compose:
```
    docker-compose up -d
```

- Go to postgres admin site in `http://localhost:8080/` and login with a `PostgreSQL` connection using `postgres` as user and password. Then add the database `company_service`.

- Run the migrations:
```
    python3 manage.py migrate
```

- Run the application:
```
    python3 manage.py runserver
```

- Create a super user
```
    python manage.py createsuperuser
```

- The admin is acessible on `admin/` resource. Signin with the super user you've just created.

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

- [Authentication](https://github.com/vision-i40/company_service/tree/master/docs/authentication)
- [User Info](https://github.com/vision-i40/company_service/tree/master/docs/user)
- [Resources HTTP Api](https://github.com/vision-i40/company_service/tree/master/docs/http_api/)
