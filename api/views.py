from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,ProductSerializer
from django.contrib.auth.models import User
from core.models import ProductVarient
@api_view(['GET'])
def userView(request):
    data=User.objects.all()
    serializer=UserSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def productView(request):
    data=ProductVarient.objects.all()
    serializer=ProductSerializer(data,many=True)
    return Response(serializer.data)


    
