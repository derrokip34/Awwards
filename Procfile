release: python manage.py makemigrations
release: python manage.py migrate

web: gunicorn awards_project.wsgi --log-file -