from django.urls import path, include
from .views import HelloAPI
from . import views


urlpatterns = [
   # USER
    path('user/ALL/', views.UserAPI),
    path('user/Detail/<str:email>', views.UserOneAPI),

    # STUDYPLAN
    # path('studyplan/list', views.StudyPlanList),

    # LIKE
    path('cert_like/<str:pk>/<str:cert_id>', views.CertificateLikeAPI),
]