# from django.shortcuts import render
# from rest_framework import viewsets, permissions, generics, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.decorators import api_view
# from .models import Certificate, User
# from .serializers import CertificateSerializer, UserSerializer

# # Create your views here.
# @api_view(['GET'])
# def HelloAPI(request):
#     return Response("hello world!")


# from api.models import Certificate
# from .serializers import CertificateSerializer

# from rest_framework import viewsets, permissions

# # Certificate Viewset
# class ListCertificates(generics.ListCreateAPIView):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer

# class DetailCertificates(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Certificate.objects.all()
#     serializer_class = CertificateSerializer

# # User Viewset
# class ListUser(generics.ListCreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# class DetailUser(generics.RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
# from ./user/serializers import UserSerializer

@api_view(['GET'])
def validate_jwt_token(request):

    try:
        token = request.META['HTTP_AUTHORIZATION']
        data = {'token': token.split()[1]}
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
    except Exception as e:
        return Response(e)

    return Response(status=status.HTTP_200_OK)