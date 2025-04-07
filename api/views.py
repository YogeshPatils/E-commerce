from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer,ProductSerializer,ProductVarientSerializer
from django.contrib.auth.models import User
from core.models import ProductVarient,Product
@api_view(['GET'])
def userView(request):
    data=User.objects.all()
    serializer=UserSerializer(data,many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
def productView(request):
    if request.method=='GET':
        data=Product.objects.all()
        serializer=ProductSerializer(data,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=ProductSerializer(data=request.data,many=isinstance(request.data,list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)

@api_view(['GET','POST'])
def productVarientView(request):
    if request.method=='GET':
        data=ProductVarient.objects.all()
        serializer=ProductVarientSerializer(data,many=True)
        return Response(serializer.data)
    if request.method=='POST':
        serializer=ProductVarientSerializer(data=request.data,many=isinstance(request.data,list))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.errors,status=400)


    
