from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Certificate, User
from .serializers import CertificateSerializer, UserSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


from api.models import Certificate
from .serializers import CertificateSerializer

from rest_framework import viewsets, permissions

# Certificate Viewset
class ListCertificates(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class DetailCertificates(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer