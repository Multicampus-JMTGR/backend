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
from user.models import User
from .serializers import CertificateSerializer, CategorySerializer, CertScheduleSerializer, CatCertSerializer, CertificateOnlySerializer, CertNameCertScheduleSerializer
from user.serializers import UserSerializer
import random
from datetime import datetime

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
    serializer_class = CertificateOnlySerializer

class DetailCertificates(generics.RetrieveUpdateDestroyAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateOnlySerializer

class ListCertCertSchedule(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

# Categories Viewset
class ListCategories(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CatCertSerializer


class DetailCategories(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CatCertSerializer


# 자격증 필터 / 검색 (자격증 이름, 시행기관) - 수녕
# http://127.0.0.1:8000/certificate/CertificatesFilter/?keyword=정보처리기사 이런식으로 요청해야함?!
@api_view(['GET'])
def CertifiacetFilterSearchAPI(request):
    value = request.GET.get('keyword')
    if request.method == 'GET':
        if value is not None: # 검색 키워드 있을 경우 - 카테고리 이름으로 검색 / 자격증 이름으로 검색 가능
            queryset = Certificate.objects.filter(Q(name__icontains=value)|Q(department__icontains=value))
            serializer = CertificateOnlySerializer(queryset, many=True)
            # queryset = Category.objects.prefetch_related('certificates').filter(Q(certificates__name__icontains=value)|Q(certificates__department__icontains=value))
        else: # 검색 키워드 없을 경우 - 전체 카테고리 + 자격증 조회
            queryset = Category.objects.all()
            serializer = CatCertSerializer(queryset, many=True)
        return Response(serializer.data)



# 추천 자격증 - 전체 자격증 중 "필기" 응시자 수 많은 순으로 8개 조회 - 수녕
class CertificateRecommendByExaminee(generics.ListAPIView):
    queryset = Certificate.objects.all().order_by('-examinee')[:8]
    serializer_class = CertificateOnlySerializer


# 추천 자격증 - 전체 자격증 중 "실기" 응시자 수 많은 순으로 8개 조회 - 수녕
class CertificateRecommendByExamineeSil(generics.ListAPIView):
    queryset = Certificate.objects.all().order_by('-examinee_sil')[:8]
    serializer_class = CertificateOnlySerializer



#추천 자격증 - 관심사 카테고리에 있는 "필기" 인기 자격증 - 수녕
@api_view(['GET'])
def CertificateRecommendByInterest(request):    
    email = request.GET.get('email')
    if email is not None: #회원
        user = User.objects.get(email=email)
        interest = user.interest #관심사항 = 카테고리명      
            # 해당 카테고리 명에 해당 하는 자격증 중에 응시수 많은 순서대로 8개 조회
        queryset = Certificate.objects.select_related('cat_id').filter(cat_id__name=interest).order_by('-examinee')[:8]
        cert_serializer = CertificateOnlySerializer(queryset, many=True)
        return Response(cert_serializer.data)
    else: #비회원
        cat_names = Category.objects.only('name') # 랜덤추출 - 카테고리이름
        size = len(cat_names) # 랜덤추출 - 사이즈
        random_num = random.randint(0,size-1) #랜덤추출 - 숫자
        random_interest = list(cat_names)[random_num] #랜덤추출 - 관심사
        
        queryset = Certificate.objects.select_related('cat_id').filter(cat_id__name=random_interest).order_by('-examinee')[:8]
        cert_serializer = CertificateOnlySerializer(queryset, many=True)
        return Response(cert_serializer.data)


#추천 자격증 - 관심사 카테고리에 있는 "실기" 인기 자격증 - 수녕
@api_view(['GET'])
def CertificateRecommendByInterestSil(request):    
    email = request.GET.get('email')
    if email is not None: #회원
        user = User.objects.get(email=email)
        interest = user.interest #관심사항 = 카테고리명      
        # 해당 카테고리 명에 해당 하는 자격증 중에 응시수 많은 순서대로 8개 조회
        queryset = Certificate.objects.select_related('cat_id').filter(cat_id__name=interest).order_by('-examinee_sil')[:8]
        cert_serializer = CertificateOnlySerializer(queryset, many=True)
        return Response(cert_serializer.data)
    else: #비회원
        cat_names = Category.objects.only('name') # 랜덤추출 - 카테고리이름
        size = len(cat_names) # 랜덤추출 - 사이즈
        random_num = random.randint(0,size-1) #랜덤추출 - 숫자
        random_interest = list(cat_names)[random_num] #랜덤추출 - 관심사
        
        queryset = Certificate.objects.select_related('cat_id').filter(cat_id__name=random_interest).order_by('-examinee_sil')[:8]
        cert_serializer = CertificateOnlySerializer(queryset, many=True)
        return Response(cert_serializer.data)



# 필기/실기 시험 결과 날짜가 임박한 자격증 정렬 / 표시하기 - 수녕
class CertificateOrderingFilter(generics.ListAPIView):
    queryset = CertSchedule.objects.select_related('cert_id').filter(result_date_1__gte=datetime.now()).order_by('result_date_1')
    serializer_class = CertNameCertScheduleSerializer 

