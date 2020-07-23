web: gunicorn hrm.wsgi:application --preload --workers 1
python manage.py collectstatic --noinput
python manage.py migrate