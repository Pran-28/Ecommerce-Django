from django.shortcuts import render

# Create your views here.


def store(request):
    context = {}
    return render(request, "ecomstore/store.html", context)


def cart(request):
    context = {}
    return render(request, "ecomstore/cart.html", context)


def checkout(request):
    context = {}
    return render(request, "ecomstore/checkout.html", context)
