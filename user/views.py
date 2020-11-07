from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import User, StudyPlan
from .serializers import UserSerializer, StudyPlanSerializer

# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


#User Insert / Select List
@api_view(['GET','POST'])
def UserAPI(request):
    if request.method == 'GET':
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Select One - 회원 존재 유무 확인 , User Update - 회원 수정 / 로그인 시 기존회원인 경우 update
@api_view(['GET','PUT'])
def UserOneAPI(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def CertificateLikeAPI(request, pk, cert_id):
    # pk값과 일치하는 유저정보 불러오기
    user = User.objects.get(id=pk)
    serializer = UserSerializer(instance=user, data=request.data)

    # 유저 instance중 cert_likes 필드에 cert_id가 이미 존재하는지 확인하기
    check_like_post = serializer.object.cert_likes.filter(cert_likes=cert_id)

    if serializer.is_valid():
        # check_like_post가 존재한다면, 자격증 없애기
        if check_like_post == True:
            serializer.object.cert_likes.remove(cert_id)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # check_like_post가 없다면, 자격증 추가하기
        else:
            serializer.object.cert_likes.add(cert_id)
            serializer.save()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 스터디 플랜 정보가 어차피 유저 안에 포함되 있어서 이게 따로 필요할진 모르겠음 일단 주석처리!
# # Study Plan List
# @api_view(['GET','POST'])
# def StudyPlanList(request):
#     if request.method == 'GET':
#         queryset = StudyPlan.objects.filter()
#         serializer = StudyPlanSerializer(queryset, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = StudyPlanSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
