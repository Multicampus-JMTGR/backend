from django.urls import path, include
from .views import HelloAPI
from . import views
# from rest_framework import routers
# from .api import CertificateViewSet

urlpatterns = [
    path('certiciate', views.ListCertificates.as_view()),
    path('certiciate/<int:pk>', views.DetailCertificates.as_view()),

]