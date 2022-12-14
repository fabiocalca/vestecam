from django.db import models
from django.conf import settings

class Product(models.Model):
  id = models.AutoField(primary_key=True)
  nome = models.CharField(max_length=255)
  descricao = models.CharField(max_length=255)
  imagem_url = models.URLField(max_length=200, null=True)
  valor = models.DecimalField(max_digits=8,decimal_places=2)
  valor_com_desconto = models.DecimalField(max_digits=8,decimal_places=2)
  desconto = models.BooleanField()
  ativo = models.BooleanField()
  quantidade = models.IntegerField()
  tamanho = models.CharField(max_length=255, null=True)
  def __str__(self):
        return f'{self.nome} ({self.tamanho})'