from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # if '' is given, it will be the default page usally the home page
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
]