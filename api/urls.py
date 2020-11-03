from django.urls import path, include
from .views import HelloAPI
from . import views
# from rest_framework import routers
# from .api import CertificateViewSet

urlpatterns = [
    path('', views.ListCertificates.as_view()),
    path('<int:pk>/', views.DetailCertificates.as_view()),

    # USER
    path('user/', views.ListUser.as_view()),
    path('user/<str:pk>', views.DetailUser.as_view()),

]