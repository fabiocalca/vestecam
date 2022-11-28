from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from .models import Product
'''
class Product(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=255)
  descricao = models.CharField(max_length=255)
  imagem_url = models.URLField(max_length=200, null=True)
  valor = models.IntegerField()
  valor_com_desconto = models.IntegerField()
  desconto = models.BooleanField()
  ativo = models.BooleanField()
  quantidade = models.IntegerField()
  tamanho = models.CharField(max_length=255, null=True)
  def __str__(self):
        return f'{self.nome} ({self.tamanho})'
'''

class ProductListView(ListView):
  model = Product
  context_object_name = 'all_products'
  template_name = 'products/index.html'

class ProductUpdateView(UpdateView):
  model = Product
  fields = ['nome', 'descricao', 'imagem_url', 'valor', 'valor_com_desconto', 'desconto', 'ativo', 'quantidade', 'tamanho']
  success_url = "/products"

class ProductDeleteView(DeleteView):
  model = Product
  success_url ="/products"
  template_name = "products/delete_confirm.html"
  
class ProductCreateView(CreateView):
  model = Product
  fields = ['nome', 'descricao', 'imagem_url', 'valor', 'valor_com_desconto', 'desconto', 'ativo', 'quantidade', 'tamanho']
  success_url = "/products"