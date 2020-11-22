from django.shortcuts import render
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
