from django.urls import path
from .views import search_product, search_products_from_xlsx, search_story

urlpatterns = [
    path('', search_story, name='main'),
    path('one/', search_product, name='one_product'),
    path('excel/', search_products_from_xlsx, name='products')
]
