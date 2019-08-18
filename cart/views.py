from django.shortcuts import render
from django.http import HttpResponse

from data.cartItems import context as cartContext
from data.itemList import context as itemContext


def add(request, item_idx):
    cartContext.append(itemContext['list'][item_idx])
    return render(request, 'cart/list.html', {'list': cartContext})


def delete(request):
    return HttpResponse('haha')
    # del context['list'][]
    # return render(request, 'cart/list.html', context)


def pay(request):
    return HttpResponse('haha')
    # return render(request, 'pay/success.html', context)
