from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def preet(request):
    return HttpResponse("<h1>This is Preet</h1>")

def home(request):
    return HttpResponse("<h1>This is home</h1>")

