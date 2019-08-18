from django.shortcuts import render

context = {
    'list': []
}
# Create your views here.


def index(request):
    return render(request, 'pay/success.html', context)
