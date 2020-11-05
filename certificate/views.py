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


# 자격증 필터 / 검색 - 수녕
# http://127.0.0.1:8000/certificate/CertificatesFilter/?keyword=정보처리기사 이런식으로 요청해야함?!
@api_view(['GET'])
def CertifiacetFilterSearchAPI(request):
    value = request.GET.get('keyword')
    if request.method == 'GET':
        queryset = Certificate.objects.all().filter(name=value).select_related('Category__cat_id')
        serializer = CertificateSerializer(queryset, many=True)
        return Response(serializer.data)


