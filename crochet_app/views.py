from django.shortcuts import render, get_list_or_404
from .models import Product, Order


# Create your views here.
def handmade(request):
    return render(
        request,
        'crochet_app/crochet.html'
    )


def orders(request):
    orders = Order.objects.all()
    return render(request, 'crochet_app/orders')


def cart(request):
    products = Product.objects.all()
