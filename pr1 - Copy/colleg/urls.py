
from django.contrib import admin
from django.urls import path
from colleg import views

urlpatterns = [
    path('home/',views.home),
]
