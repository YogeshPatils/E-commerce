from rest_framework import serializers
from django.contrib.auth.models import User
from core.models import ProductVarient,Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ['id', 'username','first_name','last_name','email']

class ProductVarientSerializer(serializers.ModelSerializer):
    class Meta:
        model=ProductVarient
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
