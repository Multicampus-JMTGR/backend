from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import User
from .serializers import UserSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


from api.models import User
from .serializers import UserSerializer

from rest_framework import viewsets, permissions

# User Viewset
class ListUser(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DetailUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

