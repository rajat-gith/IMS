from rest_framework import serializers
from src.models import *

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model=brand
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    brand=BrandSerializer(many=False)
    
    class Meta:
        model=product
        fields='__all__'

class StoreOwner_Serializer(serializers.ModelSerializer):
    class Meta:
        model=store_owner
        fields='__all__'
class StoreSerializer(serializers.ModelSerializer):
    
    brands=BrandSerializer(many=True)
    owner=StoreOwner_Serializer(many=False)
    class Meta:
        model=stores
        fields='__all__'

