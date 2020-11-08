from django.urls import path, include
from .views import HelloAPI
from . import views


urlpatterns = [
   # USER
    path('user/List/', views.UserAPIList),
    path('user/detail/<str:pk>', views.UserAPIDetail),

    # STUDYPLAN
    # path('studyplan/list', views.StudyPlanList),

    # LIKE
    path('cert_like/<str:pk>/<str:cert_id>', views.UserLikeAPIView.as_view()),
]