from django.contrib import admin
from django.urls import path
from .views import  home,about_us

urlpatterns = [
    
    path('', home),
    path('about/', about_us),


]
