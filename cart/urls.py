from django.urls import path
from django.shortcuts import render_to_response

from . import views
app_name = 'cart'
urlpatterns = [
    path('add/<int:item_idx>/', views.add, name='add-to-cart'),
    path('del/', views.delete, name='del-from-cart')
]
