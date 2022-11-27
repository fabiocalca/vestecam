from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from .models import Product
class ProductListView(ListView):
  model = Product
  context_object_name = 'all_products'
  template_name = 'products/index.html'