# DRFA
Django REST Framework (DRF) and AngularJS.

## setup virtual environment
```bash
# in project base directory
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

## create initial server
```bash
# in project base directory
django-admin startproject config server
```

## start retail application
```bash
# in server directory
python manage.py startapp retail
# after models definition
python manage.py makemigrations
python manage.py migrate
```

## server headers required for CORS(Cross-Origin Resource Sharing)
[ref](https://github.com/ottoyiu/django-cors-headers/)
