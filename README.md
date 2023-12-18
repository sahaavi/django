# django

#### Create a project in Django
```
django-admin startproject projectName
```

In django you can have one main app and subset apps of that main app. For example, instagram is the main app and direct messages, feed and insta store is subset of that app.

#### create an app
Before excuting the code below make sure you're in the root directory of your project!  
Root directory is where the manage.py lies.
```
python manage.py startapp appName
```

#### Create pages in app
create a file called urls.py inside your app directory.  
Then go to views.py to create views for each page.
Then go to the urls.py in project folder and include the urls of app.

#### Run project
```
python manage.py runserver
```

#### Set Templates
Make a folder call templates and go the project folder settings file and add the templates folder location as value in `TEMPLATES` dictionary's `DIRS` key.

```
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR, "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]
```

Now we have to change the return value of index function in `view.py` to render.