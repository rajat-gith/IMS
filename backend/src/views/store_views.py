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
