from django.shortcuts import render


def featured_products(request):
    return render(request, 'products/featured.html')


def deals(request):
    return render(request, 'products/deals.html')


def news(request):
    return render(request, 'products/news.html')
