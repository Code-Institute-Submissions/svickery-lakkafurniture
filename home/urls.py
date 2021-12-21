from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    """Frontend Path ways"""
    path('', views.index, name='home')
]
