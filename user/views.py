from django.http import request
from django.shortcuts import render


# Create your views here.

def index1(request):
    return render(request,'master.html')

def index(request):
    return render(request,'index.html')

def templateFun(request):
    return render(request,'templates.html')

def personal(request):
    return render(request,'personal.html')

def experiences(request):
    return render(request,'experiences.html')

def resume(request):
    return render(request,'resume.html')

# def resume2(request):
#     return render(request,'resume2.html')

def pricing(request):
    return render(request,'pricing.html')

def demo(request):
    return render(request,'check.html')

def premiumcheckout(request):
    return render(request,'premiumcheckout.html')