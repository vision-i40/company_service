release: python manage.py migrate --noinput
web: gunicorn company_service.wsgi --limit-request-line 8188 --log-file -
