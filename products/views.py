from django.shortcuts import render


def featured_products(request):
    return render(request, 'products/featured.html')
