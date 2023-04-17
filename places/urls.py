from django.contrib import admin
from django.urls import path
from .views import ukplaces

urlpatterns = [
    path('places/<slug:placeslug>/',ukplaces),






]
