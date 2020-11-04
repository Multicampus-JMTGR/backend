from django.urls import path, include
from .views import HelloAPI
from . import views
# from rest_framework import routers
# from .api import CertificateViewSet

urlpatterns = [
    # Certificates
    path('certificate/', views.ListCertificates.as_view()),
    path('certificate/<int:pk>', views.DetailCertificates.as_view()),

     # Category
    path('category/', views.ListCategories.as_view()),
    path('category/<int:pk>', views.DetailCategories.as_view()),
    
    # Certificates Filter - snchoi
    path('certificate/CertificatesFilter/', views.CertifiacetFilterSearchAPI),
]