from django.shortcuts import render
# from django.shortcuts import render_to_response
from django.http import HttpResponse
# from data import
from .models import ItemList
from data._itemList import context


def index(request):
    return render(request, 'items/list.html', {'list': ItemList.objects.all()})


def _importData(request):
    for item in context:
        item_temp = ItemList(
            price=item['price'],
            postal=item['postal'],
            title=item['title'],
            shopNick=item['shopNick'],
            payNum=item['payNum'],
            count=item['count'],
            image=item['image'],
        )
        item_temp.save()
    return HttpResponse('load data success')


def _delData(request):
    ItemList.objects.all().delete()
    return HttpResponse('delete data success')
