from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name="index"),
    path('master',views.index1,name='master'),
    path("templates",views.templateFun,name="templates"),
    path("personal",views.personal,name="Personal"),
    path('experiences',views.experiences,name="experiences"),
    path('resume',views.resume,name="resume"),
    # path('resume2',views.resume2,name="resume2"),
    path('pricing',views.pricing,name="pricing"),
    path('demo1',views.demo,name="demo"),
    path('premiumcheckout',views.premiumcheckout,name="premiumcheckout"),
    
]