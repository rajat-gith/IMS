from rest_framework import serializers
from src.models import *
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    _id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin']

    def get__id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if (name == ''):
            name = obj.email
        return name


class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', '_id', 'username', 'email', 'name', 'isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_brand
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)

    class Meta:
        model = product
        fields = '__all__'


class StoreOwner_Serializer(serializers.ModelSerializer):
    class Meta:
        model = store_owner
        fields = '__all__'


class StoreSerializer(serializers.ModelSerializer):

    brands = BrandSerializer(many=True)
    owner = StoreOwner_Serializer(many=False)

    class Meta:
        model = stores
        fields = '__all__'


class Sales_Serializer(serializers.ModelSerializer):
    destination_store = StoreSerializer(many=False)
    depart_store = StoreSerializer(many=False)

    class Meta:
        model = sales
        fields = '__all__'
