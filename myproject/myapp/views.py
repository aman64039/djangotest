from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Student , Course
# Create your views here.


def aman(request):
    print(request)
    return HttpResponse("<h1>My name is aman</h1>")


def home(request):
    return render(request , "myapp/aman.html" )

def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        course = request.POST["course"]
        courseid = int(course.split('_')[-1])
        course = Course.objects.get(id=courseid)
        
        std = Student(name = name , course = course)
        std.save()
        return redirect("/")
    courses = Course.objects.all()

    return render(request , "myapp/create.html"  , {'courses':courses})


def getdetails(request):
    data = Student.objects.filter(is_deleted = 0)
    return render(request , "myapp/getdetails.html" , {'data':data , "name":"Aman"} )

def update(request , id):
    std1 = Student.objects.filter(id = id)
    print("Filter  Result ", std1)
    print("\n\n")
    std = Student.objects.get(id = id)
    print("Get Result ", std)

    if request.method == "POST":
        std.name = request.POST["name"]
        std.course = request.POST["course"]
        std.save()
        return redirect("/getdetails")

    return render(request , "myapp/update.html" , {"data":std})