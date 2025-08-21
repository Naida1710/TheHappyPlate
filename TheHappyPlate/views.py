from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("The Happy Plate!")

def post_checker(request):

    if request.method == "POST":
        return HttpResponse("You must have POSTed something")
    else:
        return HttpResponse(request.method)
