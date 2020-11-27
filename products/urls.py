from django.urls import path
from . import views

urlpatterns = [
    path("", views.featured_products, name="featured"),
    path("deals", views.deals, name="deals"),
    path("news", views.news, name="news"),
    path("all-games", views.all_games, name="all-games"),
    path("search", views.search, name="search"),
    path("products/<product_id>", views.product_page, name="product_page")
]
