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
from .serializers import CertificateSerializer, CategorySerializer, CertScheduleSerializer, TestCertificateSerializer
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
        if value is not None: # 검색 키워드 있을 경우 - 카테고리 이름으로 검색 / 자격증 이름으로 검색 가능
            queryset = Category.objects.prefetch_related('certificates').filter(Q(name__icontains=value)|Q(certificates__name__icontains=value)|Q(certificates__department__icontains=value))
        else: # 검색 키워드 없을 경우 - 전체 카테고리 + 자격증 조회
            queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)



# 추천 자격증 - 전체 자격증 중 응시자 수 많은 순으로 8개 조회 - 수녕
class CertificateRecommendByExaminee(generics.ListAPIView):
    queryset = Certificate.objects.all().order_by('-examinee')[:8]
    serializer_class = CertificateSerializer


# 추천 자격증 - 관심사 카테고리에 있는 인기 자격증 - 수녕
@api_view(['GET'])
def CertificateRecommendByInterest(request, email):    
    user = User.objects.get(pk=email) # 회원정보 어떻게 가져올지...!!!!!!!!!!!!!!!!!!!(jwt봐봐)
    if user: #회원
        interest = user.interest #관심사항 = 카테고리명
        if interest is not None: #관심사항 등록한 회원            
            # 해당 카테고리 명에 해당 하는 자격증 중에 응시수 많은 순서대로 8개 조회
            queryset = Certificate.objects.select_related('cat_id').filter(cat_id__name=interest).order_by('-examinee')[:8]
            cert_serializer = CertificateSerializer(queryset, many=True)
            return Response(cert_serializer.data)
        else: #관심사항 등록하지 않은 회원(관심사항 필수일지 아닐지 아직 모름. 일단 넣어놓자)
            random()
    else: #비회원
        random()


def random(self): # 비회원의 경우 카테고리 랜덤으로 하나 고른뒤 인기 자격증 조회
    cat_names = Category.objects.only('name') # 랜덤추출 - 카테고리이름
    size = len(cat_names) # 랜덤추출 - 사이즈
    random_num = random.randint(0,size-1) #랜덤추출 - 숫자
    random_interest = list(cat_name)[random_num] #랜덤추출 - 관심사

    queryset = Certificate.objects.select_related('cat_id').filter(cat_id__name=random_interest).order_by('-examinee')[:8]
    cert_serializer = CertificateSerializer(queryset, many=True)
    return Response(cert_serializer.data)



# 필기/실시 시험 날짜가 임박한 자격증 정렬 / 표시하기 - 수녕
# 자격증 신청 마감 dday가 임박한 순서대로 정렬

# 아직 해야할 것: dday가 + 인 자격증 필터하기, 아직 신청 기간이 시작 안한 자격증 필터하기
class CertificateOrderingFilter(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = TestCertificateSerializer
    # queryset = CertSchedule.objects.select_related('cert_id').filter(test_start_date__lte=datetime.now()).values('cert_id__name', 'cert_id', 'test_round', 'test_type', 'reg_start_date', 'reg_end_date', 'test_start_date', 'test_end_date', 'result_date_1', 'result_date_2').order_by('test_start_date')
    # serializer_class = CertScheduleSerializer

    # queryset = Certificate.objects.all()
    # serializer_class = CertificateSerializer
    # filter_backends = (OrderingFilter,)
    # ordering_fields = ('test_start_date') #test_start_dday


