### Django steps

God, why do I always forget how to spin up a new Django project.

Putting some notes here in hopes I can *actually* remmember it this time.

### Prereqs

Python virtual enc


```
python3 -m venv <venv_name>
```

requirements.txt file with packages

### Commands


```
django-admin startproject <project>
```

```
django-admin startapp <app>
```

### Migrations

```
python manage.py makemigrations
```

```
python manage.py migrate
```


### Superuser
```
python manage.py createsuperuser
```

### Running
```
python manage.py runserver
python manage.py shell
```
**ENV file**
SECRET KEY
DEBUG
ALLOWED HOSTS
DJANGO APP STAGE

DB NAME
DB USER
DB PASS
DB HOST
DB PORT

**Change DB**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'your_db_name',
        'USER': 'postgres',
        'PASSWORD': 'your_db_password',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

**Create Models**
**Add app to settings***
INSTALLED_APPS - 'qppname.apps.AppNameConfig'

**Make Migrations**
**Migrate**
**Views/URLs/Routes/etc**
