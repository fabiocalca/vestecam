from rest_framework import serializers

from products.models import Product


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','nome','descricao','imagem_url','valor','valor_com_desconto','desconto','ativo','quantidade','tamanho']