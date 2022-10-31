from ast import Store
from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from src.models import brand
from src.serializer import *
# Create your views here.

@api_view(['GET'])
def getBrands(request):
    brands=brand.objects.all()
    serializer=BrandSerializer(brands,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBrandsById(request,pk):
    brands=brand.objects.get(_id=pk)
    serializers=BrandSerializer(brands,many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getProducts(request):
    products=product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data) 

@api_view(['GET'])
def getProductsById(request,pk):
    productbyId=product.objects.get(_id=pk)
    serializer=ProductSerializer(productbyId,many=False)
    return Response(serializer.data)


@api_view(['POST','GET'])
def addProduct(request):
    data=request.data
    Product=product.objects.create(
        product_name=data['product_name'],
        description=data['description'],
        brand=models['brand'],
        color=models['color'],
        category=models['category'],
        quantity=models['quantity']

    )
    serializer=ProductSerializer(Product,many=False)
    return Response(serializer.data)



