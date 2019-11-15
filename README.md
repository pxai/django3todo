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