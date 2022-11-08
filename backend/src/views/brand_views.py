from rest_framework.response import Response
from rest_framework.decorators import api_view
from src.models import *
from src.serializer import *

@api_view(['GET'])
def getBrands(request):
    queryset=brand.objects.all()
    serializer=BrandSerializer(queryset,many=True)
    return Response(serializer.data)