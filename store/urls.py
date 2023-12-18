# urls.py

from django.urls import path
from store.views import quick_add_product

urlpatterns = [
   
    path('quick_add_product/', quick_add_product, name='quickadd'),
]
