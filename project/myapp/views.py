from django.shortcuts import render
from django.http import HttpResponse

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
    return render(request, 'index.html')

def counter(request):
    text = request.GET['text']
    total_words = len(text.split())
    return render(request, 'counter.html', {'total_words': total_words})