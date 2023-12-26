from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import About

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello, world. You're at the polls index.</h1>"
    # name = "Avishek"
    # context = {
    #     'name': 'Avi',
    #     'age': 24,
    #     'hobbies': ['Coding', 'Gaming', 'Reading'],
    # }
    # return render(request, 'index.html', {'name': name})
    # return render(request, 'index.html', context)
    # return render(request, 'index.html')

    # about_1 = About()
    # about_1.name = "Avishek"
    # about_1.details = "I am a data scientist"
    # about_1.phone = 1234
    # about_1.email = "as@gmail.com"

    # about_2 = About()
    # about_2.name = "Saha"
    # about_2.details = "I am a data analyst"
    # about_2.phone = 1234
    # about_2.email = "saha@gmail.com"

    # abouts = [about_1, about_2]

    # return render(request, 'index.html', {'about1': about_1, 'about2': about_2})
    # return render(request, 'index.html', {'abouts': abouts})
    
    # importing data from database
    abouts = About.objects.all()
    return render(request, 'index.html', {'abouts': abouts})

# Counter for GET method
# def counter(request):
#     text = request.GET['text']
#     total_words = len(text.split())
#     return render(request, 'counter.html', {'total_words': total_words})

# Counter for POST method
def counter(request):
    text = request.POST['text']
    total_words = len(text.split())
    return render(request, 'counter.html', {'total_words': total_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already In Use')
                # return render(request, 'register.html')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already In Use')
                # return render(request, 'register.html')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.info(request, 'User Created')
                # return render(request, 'login.html')
                return redirect('login')
        else:
            messages.info(request, 'Password Not Matching')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')