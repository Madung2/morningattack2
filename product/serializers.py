from rest_framework import serializers
from product.models import Item as ItemModel
from product.models import Category as CategoryModel
from product.models import Product as ProductModel

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = CategoryModel
        fields = ['name']

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)

    class Meta:
        model = ItemModel
        fields = ['name', 'thumnail', 'category', 'orders']


class OrderSerializer(serializers.ModelSerializer):
    