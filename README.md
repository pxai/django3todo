## Django setup
Install django with:

```shell
python -m pip install Django
```

## Create the app
```shell
 django-admin startproject project-name
```

Running the app
```shell
 python manage.py runserver
```
Open site at http://localhost:8000

## Add app

Open settings.py and add

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.AppConfig', 
]
```

# Add urls for app
Open urls.py and add:
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('todo.urls')),
]
```
## Add statics to url
Django doesn't serve them by default but:
```python
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

## Add migrations
Add models to the app, then:
```shell
python3 manage.py makemigrations todo
python3 manage.py migrate
```

The last one will apply migration things

## Creating models

By default models shuould be placed in `models.py` 

### Creating task

```python
a_record = Todo(task="Learn Django")
```

# Guardar el objeto en la base de datos.
```
a_record.save()
```

## Templates
First we need to define where we store templates
in settings.py
```python
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            './todo/views/templates',
        ],
    },
    {
        'BACKEND': 'django.template.backends.jinja2.Jinja2',
        'DIRS': [
            '/home/html/jinja2',
        ],
    },
]
```

```python
```

## Fixtures
With fixtures we can load initial data.
Set it in a fixtures directory in yaml or json and then
run:

```shell
 manage.py loaddata fixture_file
```

## Setting translations
In code we use gettext with `_`.
Set this option in `settings.py` to activate i18n and default lang:
```python
USE_I18N = True
LANGUAGE_CODE = 'en-us'
```
Also define languages that you want to support
```python
LANGUAGES = (
    ('en', _('English')),
    ('es', _('Spanish')),
    ('fr', _('French')),
)
```

Also in theory you could set up a locale directory:
```python
LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'i18n'),
)
```
But WHAT it WORKED was to create `project_root/app/locale/en` directory.


Yoou can let django to generate po files, it will check all you code to search messages
that can be translated.
```python
django-admin.py makemessages --extension=html,py --locale=en --all
```
Or multiple at the same time (try inside app dir)
```python
/usr/local/bin/python3.7 /home/pello/.local/bin/django-admin.py  makemessages --extension=html,py -l en -l es --all
```

Make sure that you have defined LOCALE_PATHS or you'll get a message lik
``
CommandError: Unable to find a locale path to store translations for file manage.py`
```
Then we have to compile messages with:
```python
django-admin compilemessages
```

Then we need to organize po files in the defined directory, with this format:
`lang.po` for example: `en.po`
Optionally you can use [poeditor](https://snapcraft.io/poedit)
## The admin app
You must set admin options in admin.py

```python
from django.contrib import admin
from .models import Todo, TaskType
# Register your models here
admin.site.register(Todo)
admin.site.register(TaskType)
```
You must create a superuser:
```shell
python3 manage.py createsuperuser
```

```python
```

```python
```