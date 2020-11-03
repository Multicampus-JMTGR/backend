from django.urls import path, include
from .views import HelloAPI
from . import views


from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token #jwt위해 추가
from .views import validate_jwt_token #jwt위해 추가


urlpatterns = [
    # path('', views.ListCertificates.as_view()),
    # path('<int:pk>/', views.DetailCertificates.as_view()),

    # # USER
    # path('user/', views.ListUser.as_view()),
    # path('user/<str:pk>', views.DetailUser.as_view()),

    path('validate/', validate_jwt_token), #JWT를 받아 토큰을 검증하여 상태코드로 반환
    path('login/', obtain_jwt_token), #Google의 ID 토큰을 받아 JWT를 반환
    
    path('verify/', verify_jwt_token), 
    path('refresh/', refresh_jwt_token), #JWT를 받아 토큰을 검증하여 새로운 토큰 반환

]