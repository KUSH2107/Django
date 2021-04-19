from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from college import views

urlpatterns = [
    path('college/', include('college.urls')),
    path('admin/', admin.site.urls),
]
