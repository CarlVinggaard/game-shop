from django.shortcuts import render, get_object_or_404, redirect, reverse
from .models import Product
from django.db.models import Q


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


def search(request):
    if request.GET:
        if 'query' in request.GET:
            query = request.GET['query']
            if not query:
                return redirect(reverse('featured'))

            queries = Q(name__icontains=query) | Q(description__contains=query)
            products = Product.objects.filter(queries)

            context = {"products": products, "query": query}

            return render(request, "products/search.html", context)


def product_page(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    context = {"product": product}

    return render(request, 'products/product_page.html', context)
