from django.shortcuts import render, get_object_or_404
from .models import Product


def featured_products(request):
    products = Product.objects.filter(featured=True).all()

    context = {"products": products}

    return render(request, "products/featured.html", context)


def deals(request):
    return render(request, "products/deals.html")


def news(request):
    return render(request, "products/news.html")


def all_games(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "products/all_games.html", context)


def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}

    return render(request, 'products/product_page.html', context)
