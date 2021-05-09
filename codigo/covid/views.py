from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    return render(request, 'home.html',{})

def admin_view(request, *args, **kwargs):
    return render(request, 'admin.html',{})