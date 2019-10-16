release: python3 manage.py migrate
web: gunicorn company_service.wsgi --limit-request-line 8188 --log-file -
