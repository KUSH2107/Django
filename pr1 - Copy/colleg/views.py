from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

def home(req):
    return HttpResponse("<h1>Hey Kush!</h1>")

    
