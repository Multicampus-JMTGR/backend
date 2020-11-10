from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from .models import User, StudyPlan
from .serializers import UserSerializer, StudyPlanSerializer, UserLikesSerializer, UserLikesStudySerializer


# Create your views here.
@api_view(['GET'])
def HelloAPI(request):
    return Response("hello world!")


#User Insert / Select List - snchoi
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


class ListUsersLikes(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserLikesSerializer

# User Select One - 회원 존재 유무 확인 , User Update - 회원 수정 / 로그인 시 기존회원인 경우 update
@api_view(['GET','PUT', 'POST'])
def UserOneAPI(request, email):
    try:
        queryset = User.objects.get(email=email)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = UserLikesStudySerializer(queryset)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UserLikesStudySerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# # 스터디 플랜 정보가 어차피 유저 안에 포함되 있어서 이게 따로 필요할진 모르겠음 일단 주석처리!
# Study Plan List
@api_view(['GET','POST'])
def StudyPlanList(request):
    if request.method == 'GET':
        queryset = StudyPlan.objects.filter()
        serializer = StudyPlanSerializer(queryset, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudyPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


      
# 좋아요 구현
@api_view(['GET', 'POST'])
def CertificateLike(request, email, cert_id):
    user = User.objects.get(email=email)
    like_posts = user.cert_likes.filter(cert_id=cert_id)
    # serializer = UserLikesSerializer(user)
    if like_posts.exists():
        user.name = user.name
        user.interest = user.interest
        user.email = user.email
        user.phone_number = user.phone_number
        user.cert_likes.remove(cert_id)
        user.save()
        serializer = UserLikesSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        user.name = user.name
        user.interest = user.interest
        user.email = user.email
        user.phone_number = user.phone_number
        user.cert_likes.add(*cert_id)
        user.save()
        serializer = UserLikesSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




## USER LIST 호출 하는 다른 방법 ###


# class DetailUsers(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserLikesStudySerializer

