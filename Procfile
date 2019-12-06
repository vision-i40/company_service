web: gunicorn company_service.wsgi --limit-request-line 8188 --log-file -
release: python3 manage.py migrate --no-input
