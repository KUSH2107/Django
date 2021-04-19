
from django.contrib import admin
from django.urls import path
from college import views

urlpatterns = [
    path('home/',views.home ),
    path('about/',views.about),
    path('contect/',views.contect),
]
