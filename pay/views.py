from django.shortcuts import render
from data.itemList import context as itemContext
from data.cartItems import context as cartContxt


def index(request):
    if request.method == 'POST':
        for itemIdx in cartContxt.keys():
            itemContext[itemIdx]['count'] -= cartContxt[itemIdx]['count']
        cartContxt.clear()
    return render(request, 'pay/success.html', {})
