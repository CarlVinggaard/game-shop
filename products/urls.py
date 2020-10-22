from django.urls import path
from . import views

urlpatterns = [
  path('featured', views.featured_products, name='featured'),
]
