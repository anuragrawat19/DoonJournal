from django.contrib import admin
from django.urls import path
from .apiviews import contactus_api

urlpatterns = [
    
    path('contact-us/', contactus_api),



]
