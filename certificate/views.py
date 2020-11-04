from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Certificate, User, Category
from .serializers import CertificateSerializer, CategorySerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


from .models import Certificate
from .serializers import CertificateSerializer

from rest_framework import viewsets, permissions

# Certificate Viewset
class ListCertificates(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer(queryset, many=True)

class DetailCertificates(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer(queryset, many=True)


class ListCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer(queryset, many=True)
