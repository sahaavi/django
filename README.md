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

TO add the app to the project go to the project settings file and add `myapp` in `INSTALLED APPS`  

To save the changes in app's model file and make it a database we need to run the command `python manage.py makemigrations` then `python manage.py migrate`
So it sends the data to django database

We can check it in django admin panel.
admin panel url: http://127.0.0.1:8000/admin  

But we don't have any credentials so we have to create the superuser now.
Run the command below  
`python manage.py createsuperuser`

We have to register the model databse in `admin.py` of our app in order to see it in the admin panel.

Now we can add data from the admin panel.

#### Dynamic URL Routing
Make a path in app urls.py
`path('post/<str:pk>, views.post, name='post')`
Then make the post function in views
```python
def post(request, pk):
    return render(request, 'post.html', {'pk': pk})
```
Make the post.html file inside template
```html
<h1>The value in the url is {{pk}}</h1>
```
Now you will get whatever you want as you pass after this post http://127.0.0.1:8000/post/

#### Connect to PostgreSQL Database
goto projects settings.py & modify the `DATABASES` variable

change the engine to postgresql & change the name to your database name

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django",
        "USER": 'postgres',
        "PASSWORD": '',
        "HOST": 'localhost'
    }
}
```

Then isntall 2 packages 'psycopg2' & 'Pillow'. Now execute the command below:
`python manage.py makemigrations` then `python manage.py migrate`