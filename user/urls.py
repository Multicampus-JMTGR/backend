from django.urls import path, include
from .views import HelloAPI
from . import views


urlpatterns = [
   # USER
    path('user/ALL/', views.UserAPI),
    path('user/Detail/<str:email>', views.UserOneAPI),

    # STUDYPLAN
    # path('studyplan/list', views.StudyPlanList),

    # 좋아요 구현 방법 1
    path('cert_like_1/<str:pk>/<str:cert_id>', views.LikeUpdate_1),

    # 좋아요 구현 방법 2
    path('cert_like_2', views.LikeUpdate_2.as_view()),
]