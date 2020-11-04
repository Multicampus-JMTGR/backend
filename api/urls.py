from django.urls import path, include
from .views import HelloAPI
from . import views


from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token, refresh_jwt_token #jwt위해 추가
from .views import validate_jwt_token #jwt위해 추가


urlpatterns = [
    path('validate/', validate_jwt_token), #JWT를 받아 토큰을 검증하여 상태코드로 반환
    path('login/', obtain_jwt_token), #Google의 ID 토큰을 받아 JWT를 반환 / user_name, password를 보내면 response로 token이 생성된다.
    
    path('verify/', verify_jwt_token), # 가지고 있는 token에대해서 verify합니다.
    path('refresh/', refresh_jwt_token), #JWT를 받아 토큰을 검증하여 새로운 토큰 반환 / token이 살아있다는 전제하에 새로운 토근값을 받을 수 있습니다.
]