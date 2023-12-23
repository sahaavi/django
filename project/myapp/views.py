from django.shortcuts import render
from django.http import HttpResponse
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
    about_1 = About()
    about_1.name = "Avishek"
    about_1.details = "I am a data scientist"
    about_1.phone = 1234
    about_1.email = "as@gmail.com"

    about_2 = About()
    about_2.name = "Saha"
    about_2.details = "I am a data analyst"
    about_2.phone = 1234
    about_2.email = "saha@gmail.com"

    abouts = [about_1, about_2]

    # return render(request, 'index.html', {'about1': about_1, 'about2': about_2})
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