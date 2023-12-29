from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # if '' is given, it will be the default page usally the home page
    path('counter', views.counter, name='counter'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('post/<str:pk>', views.post, name='post'), 
    # path('post/<int:pk>', views.post, name='post') # if int is given, it will only accept integer value)
    path('dynamic', views.dynamic, name='dynamic')
]