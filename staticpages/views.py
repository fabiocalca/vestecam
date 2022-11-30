from django.shortcuts import render
from cart.cart import Cart

def index(request):
    context = {'cart': Cart(request)}
    return render(request, 'staticpages/index.html', context)


def about(request):
    context = {}
    return render(request, 'staticpages/about.html', context)