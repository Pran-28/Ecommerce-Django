from django.shortcuts import render
from .models import *
# Create your views here.


def store(request):
    products = Product.objects.all()
    print('products===>', products)
    context = {'products':products}
    return render(request, "ecomstore/store.html", context)


def cart(request):
    context = {}
    return render(request, "ecomstore/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "ecomstore/checkout.html", context)
