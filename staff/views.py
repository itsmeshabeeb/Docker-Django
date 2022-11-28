from django.http import request
from django.shortcuts import render


# Create your views here.
# def dashboard(request):
#     return render(request,'dashboard.html')

def stafflogin(request):
    return render(request,'stafflogin.html')

def staffmaster(request):
    return render(request,'masterstaff.html')

def dashboard(request):
    return render(request,'dashboard.html')

def userdetails(request):
    return render(request,'userdetails.html')

def templatedetails(request):
    return render(request,'templatedetails.html')

def templatedatas(request):
    return render(request,'templatedatas.html')

def reports(request):
    return render(request,'report.html')

def pricing(request):
    return render(request,'pricingpage.html')