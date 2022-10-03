from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def Home_view(request, *args, **kwargs):
    # return HttpResponse("<h1> Hello </h1>")
    return render(request, "home.html", {})


def Main_view(request, *args, **kwargs):
    return render(request, "index.html", {})
