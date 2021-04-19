from django.shortcuts import render
from college.models import Notice
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

# Create your views here.
def home(req):
    return render(req, "index.html")
    
class NoticeListView(ListView):
    model = Notice

class NoticeDetailView(DetailView):
    model = Notice