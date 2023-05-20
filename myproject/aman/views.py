from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aman(request):
    return HttpResponse("<h1>This is aman</h1>")

def home(request):
    return HttpResponse("<h1>This is home</h1>")


