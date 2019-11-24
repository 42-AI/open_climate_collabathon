

### install:
```
pip install -r requirements.txt
```

## run locally:
```
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
and go to 127.0.0.1:8000 to test it localy

To use another IP address and serve on your network, simply add it to ALLOWED_HOSTS in settings.py and run with: 
```
python manage.py runserver IP
```

## usage
To append data, connect to admin pannel and go to "MAP" section, click first item ("Data files") and add a ".xlsx" file formated as demo file provided and a country TAG (3 letters).
Data will populate DB and will be available to access (edit and remove from admin pannel).


