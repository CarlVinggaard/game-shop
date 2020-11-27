from django.shortcuts import render, get_object_or_404
from .models import Product


def featured_products(request):
    products = Product.objects.filter(featured=True).all()

    context = {"products": products}

    return render(request, "products/featured.html", context)


def deals(request):
    products = Product.objects.filter(deal__gte=0).all()

    context = {"products": products}

    return render(request, "products/deals.html", context)


def news(request):
    products = Product.objects.filter(release_year__gte=2015).all()

    context = {"products": products}

    return render(request, "products/news.html", context)


def all_games(request):
    products = Product.objects.all()

    context = {"products": products}

    return render(request, "products/all_games.html", context)


def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}

    return render(request, 'products/product_page.html', context)
