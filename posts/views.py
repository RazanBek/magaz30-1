from django.shortcuts import HttpResponse, render
from datetime import datetime
from .models import Product, Category


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


def categoryes_view(request):
    if request.method == 'GET':
        categoryes = Category.objects.all()

        context_data = {
            'categoryes': categoryes
        }

        return render(request, 'products/categoryes/categoryes.html', context=context_data)


def product_detail_view(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)

        context_data = {
            "product": product
        }
        return render(request, 'products/detail.html', context=context_data)

