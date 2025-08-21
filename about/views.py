from django.shortcuts import render
from django.http import HttpResponse

def about_us(request):
    return HttpResponse("About Us page")

# Create your views here.
