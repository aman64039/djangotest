from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def aman(request):
    print(request)
    return HttpResponse("<h1>My name is aman</h1>")


def home(request):
    return render(request , "myapp/aman.html" )
