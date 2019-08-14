from django.urls import path
from django.shortcuts import render_to_response

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
