from django.urls import path
from django.shortcuts import render_to_response

from . import views

app_name = 'items'
urlpatterns = [
    path('', views.index, name='index'),
    path('internal/import-all', views._importData, name='internal-add'),
    path('internal/del-all', views._delData, name='internal-del')
]
