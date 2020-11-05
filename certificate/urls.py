from django.urls import path, include
from .views import HelloAPI
from . import views

urlpatterns = [
    # Certificates
    path('certificate/', views.ListCertificates.as_view()),
    path('certificate/<int:pk>', views.DetailCertificates.as_view()),

     # Category
    path('category/', views.ListCategories.as_view()),
    path('category/<int:pk>', views.DetailCategories.as_view()),
    
    # Certificates Filter - snchoi
    path('certificate/CertificatesFilter/', views.CertifiacetFilterSearchAPI),

    # Certificate Ordering Filter - minji
    path('certificate/OrderingFilter', views.CertificateOrderingFilter.as_view())

]
