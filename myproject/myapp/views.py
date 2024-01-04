from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello")

def myfunctionabout(request):
    return HttpResponse("About Response")

def add(request, a, b):
    return HttpResponse(a+b)

def intro(request, name, age):
    dict = {"name":name,
            "age": age}
    return JsonResponse(dict)

def myfirstpage(request):
    return render(request, "index.html")

def mysecondpage(request):
    return render(request, "second.html")