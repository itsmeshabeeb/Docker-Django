from django.urls import path
from .import views

urlpatterns = [
    path('stafflogin',views.stafflogin, name="stafflogin"),
    path('staffmaster',views.staffmaster, name='staffmaster'),
    path('dashboard',views.dashboard, name='dashboard'),
    path('userdetails',views.userdetails, name='userdetails'),
    path('templatedetails',views.templatedetails, name='templatedetails'),
    path('templatedatas',views.templatedatas, name='templatedatas'),
    path('report',views.reports, name='report'),
    path('pricingpage',views.pricing, name='pricingpage'),
]