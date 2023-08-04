from django.db.models import Q
from django.shortcuts import render, redirect

from .models import Product, Category, Review
from posts.forms import ProductCreateForm, CategoryCreateForm, ReviewCreateForm
from posts.constans import PAGINATION_LIMIT


def main_view(request):
    if request.method == 'GET':
        return render(request, 'layouts/main.html')


def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()

        max_page = products.__len__() / PAGINATION_LIMIT
        if round(max_page) < max_page:
            max_page = round(max_page) + 1
        else:
            max_page = round(max_page)

        search_text = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        if search_text:
            products = products.filter(Q(name__icontains=search_text) |
                                       Q(description__icontains=search_text))

        """ Pagination """
        products = products[PAGINATION_LIMIT * (page - 1):PAGINATION_LIMIT * page]

        context_data = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, 'products/products.html', context=context_data)


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


def product_create_view(request):
    if request.method == "GET":
        context_data = {
            'form': ProductCreateForm
        }

        return render(request, 'products/create.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = ProductCreateForm(data, files)

        if form.is_valid():
            Product.objects.create(
                img = form.cleaned_data.get('img'),
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
            )
            return redirect('/products/')

        return render(request, 'products/create.html', context={
            'form': form
        })


def category_create_view(request):
    if request.method == "GET":
        context_data = {
            'form': CategoryCreateForm
        }

        return render(request, 'products/categoryes/categoryes.html', context=context_data)

    if request.method == 'POST':
        data, files = request.POST, request.FILES
        form = CategoryCreateForm(data, files)

        if form.is_valid():
            Category.objects.create(
                name=form.cleaned_data.get('name'),
            )
            return redirect('/categoryes/')

        return render(request, 'products/categories.html', context={
            'form': form
        })


def review_create_view(request):
    if request.method == 'GET':
        context_data = {
            'form': ReviewCreateForm
        }

        return render(request, 'products/detail.html', context=context_data)

    if request.method == 'POST':
        data = request.POST
        form = ReviewCreateForm(data)

        if form.is_valid():
            Review.objects.create(
                review=form.cleaned_data.get('review'),
            )
            return redirect('/products/detail/')

        return render(request, 'products/detail.html', context={
            'form': form
        })


