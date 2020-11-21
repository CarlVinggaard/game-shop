from django.urls import path
from . import views

urlpatterns = [
    path("", views.featured_products, name="featured"),
    path("deals", views.deals, name="deals"),
    path("news", views.news, name="news"),
]
