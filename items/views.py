from django.shortcuts import render
# from django.shortcuts import render_to_response
from django.http import HttpResponse
# from data import
from .models import ItemList


def index(request):
    return render(request, 'items/list.html', {'list': ItemList.objects.all()})
