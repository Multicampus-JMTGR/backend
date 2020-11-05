from django.shortcuts import render
from rest_framework import viewsets, permissions, generics, status, filters
from django_filters import rest_framework as filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from django.db.models import Q
from .models import Certificate, Category, CertSchedule
from .serializers import CertificateSerializer, CategorySerializer, CertScheduleSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")

from rest_framework import viewsets, permissions

# Schedule Viewset
class ListCertSchedule(generics.ListCreateAPIView):
    queryset = CertSchedule.objects.all()
    serializer_class = CertScheduleSerializer

class DetailCertSchedule(generics.RetrieveUpdateDestroyAPIView):
    queryset = CertSchedule.objects.all()
    serializer_class = CertScheduleSerializer

# Certificate Viewset
class ListCertificates(generics.ListCreateAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class DetailCertificates(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer


# Categories Viewset
class ListCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# 자격증 필터 / 검색 (자격증 이름, 시행기관) - 수녕
# http://127.0.0.1:8000/certificate/CertificatesFilter/?keyword=정보처리기사 이런식으로 요청해야함?!
@api_view(['GET'])
def CertifiacetFilterSearchAPI(request):
    value = request.GET.get('keyword')
    if request.method == 'GET':
        if value is not None: # 검색 키워드 있을 경우 - 카테고리 이름으로 검색해도 나오게 하고싶은데 Inner Join 더 찾아봐야 할것같음
            queryset = Certificate.objects.filter(Q(name__icontains=value)|Q(department__icontains=value))#.select_related('Category__cat_id')
            #queryset = Certificate.objects.prefetch_related('Category__cat_id')
        else: #검색 기워드 없을 경우 자격증 전체 조회 - 카테고리별로 보여줘야하기 때문에 얘도 inner join 필요
            queryset = Certificate.objects.all()
        serializer = CertificateSerializer(queryset, many=True)
        return Response(serializer.data)

# 추천 자격증 - 응시자 수
class CertificateRecommendByExaminee(generics.ListAPIView):
    queryset = Certificate.objects.all().order_by('-examinee')[:8]
    serializer_class = CertificateSerializer


# 추천 자격증 - 관심사 카테고리에 있는 인기 자격증



# 날짜가 임박한 자격증 정렬 / 표시하기 - 민지
# 자격증 신청 마감 dday가 임박한 순서대로 정렬

# 아직 해야할 것: dday가 + 인 자격증 필터하기, 아직 신청 기간이 시작 안한 자격증 필터하기
class CertificateOrderingFilter(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    filter_backends = [ filters.OrderingFilter ]
    ordering_fields = ['reg_end_dday']

