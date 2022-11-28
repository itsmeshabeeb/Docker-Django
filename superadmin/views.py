from django.http import request
from django.shortcuts import render

# Create your views here.

def masteradmin(request):
    return render(request,'masteradmin.html')

def admindash(request):
    return render(request,'admindash.html')
