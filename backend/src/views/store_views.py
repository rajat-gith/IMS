from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from src.models import *
from src.serializer import *


@api_view(['GET'])
def getStores(request):
    query = request.query_params.get('keyword')
    if (query == None):
        query = ''
    queryset = stores.objects.filter(name__icontains=query)
    serializer = StoreSerializer(queryset, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStoreOwners(request):
    owners = store_owner.objects.all()
    serializer = StoreOwner_Serializer(owners, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getStoreById(request, pk):
    store = stores.objects.get(_id=pk)
    serializer = StoreSerializer(store, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getStoreOwnerById(request, pk):
    owner = store_owner.objects.get(_id=pk)
    serializers = StoreOwner_Serializer(owner, many=False)
    return Response(serializers.data)


@api_view(['GET'])
def getSales(request):
    sales_records = sales.objects.all()
    serializers = Sales_Serializer(sales_records, many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getSalesById(request, pk):
    sales_record = sales.objects.get(_id=pk)
    serializers = Sales_Serializer(sales_record, many=False)
    return Response(serializers.data)


@api_view(['GET', 'POST'])
def creatSales(request):
    data = request.data
    NewSales = sales.objects.create(
        date_of_dispatch=data['date'],
        quantity_shipment=data['quantity']
    )

    destination_store_obj = stores.objects.get(name=(data['destination']))
    source_store_obj = stores.objects.get(name=data['source'])

    NewSales.destination_store = destination_store_obj
    NewSales.depart_store = source_store_obj

    NewSales.save()
    serializer = Sales_Serializer(NewSales, many=False)
    return (Response(serializer.data))


@api_view(['POST'])
def createStoreBrand(request, pk):
    store = stores.objects.get(_id=pk)
    data = request.data
    Brand = Product_brand.object.create(
        name=data['name'],
        quantity=data['quantity'],
        status=data['status']
    )

    brands = stores.brand_set.all()
