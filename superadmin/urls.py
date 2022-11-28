from django.urls import path
from .import views


urlpatterns = [
   path('masteradmin',views.masteradmin, name='masteradmin'),
   path('admindash',views.admindash, name='admindash'),
     
]