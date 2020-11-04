from django.shortcuts import render
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


#User Insert/Select List
@api_view(['GET','POST'])
def UserAPIList(request):
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

# User Select One
@api_view(['GET'])
def UserAPIDetail(request, pk):
    try:
        queryset = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserSerializer(queryset)
        return Response(serializer.data)

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
