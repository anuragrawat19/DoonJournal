from django.contrib import admin
from django.urls import path
from .views import  home,about_us,contact_us

urlpatterns = [
    
    path('', home),
    path('about/', about_us),
    path('contact-us/', contact_us),



]
