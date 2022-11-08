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
    color=data['color']
    category=data['category']
    
    for i in range(0,len(color)):
        if(colors[i][0]==color):
            color_index=i
    
    for i in range(0,len(categorys)):
        if(categorys[i][0]==category):
            category_index=i
            
    Product=product.objects.create(
        product_name=data['product_name'],
        description=data['description'],
        color=colors[color_index][0],
        category=categorys[category_index][0],
        quantity=data['quantity'],
        price=data['price']
    )
    print(data['brand']['_id'])
    for brand in data['brand']['_id']:
        brand_obj=brand.objects.get(_id=brand)
        Product.brand.add(brand_obj)

    print("P->",data['brand'])
    # print(brand.objects.get(_id=data['brand']))
    # print(data['brand'])
    
    
    serializer=ProductSerializer(Product,many=False)
    return Response(serializer.data)



