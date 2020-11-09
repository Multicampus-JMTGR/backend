from django.urls import path, include
from .views import HelloAPI
from . import views


urlpatterns = [
   # USER
   # 좋아요 정보는 PK만 표시
   path('api/user', views.ListUsers.as_view()),
   # 좋아요 한 자격증, 카테고리 정보도 상세하게 표시
    path('api/user/detail', views.ListUsersLikes.as_view()),
    # 유저 한명의 데이터만 표시
    path('api/user/<str:pk>', views.DetailUsers.as_view()),

    # STUDYPLAN
    path('api/studyplan', views.StudyPlanList),

    # CERTIFICATE LIKE
    path('cert_like/<str:email>/<str:cert_id>', views.CertificateLike),

]