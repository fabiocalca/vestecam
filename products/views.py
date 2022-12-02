from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Product
import requests
from cart.cart import Cart

class ProductListView(ListView):
  model = Product
  context_object_name = 'all_products'
  template_name = 'products/index.html'
  extra_context={}

class ProductUpdateView(UpdateView):
  model = Product
  fields = ['nome', 'descricao', 'imagem_url', 'valor', 'valor_com_desconto', 'desconto', 'ativo', 'quantidade', 'tamanho']
  success_url = "/products/"

class ProductDeleteView(DeleteView):
  model = Product
  success_url ="/products/"
  template_name = "products/delete_confirm.html"
  
class ProductCreateView(CreateView):
  model = Product
  fields = ['nome', 'descricao', 'imagem_url', 'valor', 'valor_com_desconto', 'desconto', 'ativo', 'quantidade', 'tamanho']
  success_url = "/products/"