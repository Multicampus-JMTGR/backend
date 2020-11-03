from django.urls import path, include
from .views import HelloAPI
from . import views
# from rest_framework import routers
# from .api import CertificateViewSet

urlpatterns = [
   # USER
    path('user/', views.ListUser.as_view()),
    path('user/<str:pk>', views.DetailUser.as_view()),
]