from django.shortcuts import HttpResponse, render
from datetime import datetime
from .models import Product


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        context_data = {
            'products': products
        }
        return render(request, 'products/products.html', {'products': products})