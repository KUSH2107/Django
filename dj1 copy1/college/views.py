from django.shortcuts import render


# Create your views here.
def home(req):
    return render(req,"home.html",{"name":"kush"})

def about(req):
    return render(req,"about.html")

def contect(req):
    return render(req,"contect.html")    

