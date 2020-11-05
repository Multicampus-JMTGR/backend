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
from .serializers import CertificateSerializer, CategorySerializer, CertScheduleSerializer
from user.serializers import UserSerializer


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


# 추천 자격증 - 전체 자격증 중 응시자 수 많은 순으로 8개 조회 - 수녕
class CertificateRecommendByExaminee(generics.ListAPIView):
    queryset = Certificate.objects.all().order_by('-examinee')[:8]
    serializer_class = CertificateSerializer


# 추천 자격증 - 관심사 카테고리에 있는 인기 자격증 - 수녕
class CertificateRecommendByInterest(generics.ListAPIView):
    interest = '정보기술'#request.GET.get('keyword')
    queryset = Category.objects.filter(name=interest)

    serializer_class = CategorySerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('-examinee') # 내림차순 해야되는데 왜안돼....

# @api_view(['GET'])
# def CertificateRecommendByInterest(request):
#     # interest = request.GET.get('keyword')
#     # queryset = Category.objects.filter(name=interest)#.order_by('certificates__-examinee')[:8]
#     # serializer = CategorySerializer(queryset, many=True)
#     # serializer.objects.certificates.OrderingFilter
#     # return Response(serializer.data)
    
    
    
#     user = User.objects.get(pk=pk)
#     user_serializer = UserSerializer(instance=user, data=request.data)
#     if user: #회원
#         interest = user.interest #관심사항 = 카테고리명
#         if interest is not None: #관심사항 등록한 회원            
#             # 해당 카테고리 명에 해당 하는 자격증 중에 응시수 많은 순서대로 8개 조회
#             queryset = Category.objects.filter(name=interest).order_by('-examinee')[:8]
#             cat_serializer = CategorySerializer(queryset, many=True)
#             return Response(cat_serializer.data)

#         else: #관심사항 등록하지 않은 회원
#             # 카테고리명 랜덤으로 고름

#             # 해당 카테고리 명에 해당하는 자격증 중에 응시수 많은 순서대로 8개 조회
#     else: #비회원
#         # 카테고리명 랜덤으로 고름
#         Category
        
#         # 해당 카테고리 명에 해당하는 자격증 중에 응시수 많은 순서대로 8개 조회
        






# 날짜가 임박한 자격증 정렬 / 표시하기 - 민지
# 자격증 신청 마감 dday가 임박한 순서대로 정렬

# 아직 해야할 것: dday가 + 인 자격증 필터하기, 아직 신청 기간이 시작 안한 자격증 필터하기
# 그럼 필기시험 일자 디데이, 실기시험일자 디데이 적게 남은 순서대로 10개정도만 보여줄까?
class CertificateOrderingFilter(generics.ListAPIView):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
    filter_backends = (OrderingFilter,)
    ordering_fields = ('test_start_date') #test_start_dday


