from rest_framework import serializers
from main.models.auth import User
from main.models.core import Product, Product_Images, Category


class User_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class Category_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class Product_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class Images_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_Images
        fields = '__all__'
      

