from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, "index.html")

def blog(request):
    return render(request, "blog.html")

def test(request):
    return render(request, "test.html")

def login(request):
    return render(request, "login.html")

def aboutus(request):
    return render(request, "test.html")

def services(request):
    return render(request, "test.html")

def search(request):
    return render(request, "test.html")

def register(request):
    return render(request, "test.html")

def college(request):
    return render(request, "test.html")