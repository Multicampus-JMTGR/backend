from django.urls import path, include
from .views import HelloAPI
from . import views

urlpatterns = [

    # Certificate Schedule
    path('api/certschedule/', views.ListCertSchedule.as_view()),
    path('api/certschedule/<int:pk>', views.DetailCertSchedule.as_view()),
    
    # Certificates
    path('api/certificate/', views.ListCertificates.as_view()),
    path('api/certificate/<int:pk>', views.DetailCertificates.as_view()),

    # Category
    path('api/category/', views.ListCategories.as_view()),
    path('api/category/<int:pk>', views.DetailCategories.as_view()),
    
    # Certificates Filter - snchoi
    path('api/certificate/CertificatesFilter/', views.CertifiacetFilterSearchAPI),

    # Certificate Ordering Filter - snchoi
    path('api/certificate/OrderingFilter/', views.CertificateOrderingFilter.as_view()), #테스트중

    # CertificateRecommand By 필기 Examinee - snchoi
    path('api/certificate/CertRecomByExaminee/', views.CertificateRecommendByExaminee.as_view()),

    # CertificateRecommand By 실기 Examinee - snchoi
    path('api/certificate/CertRecomByExamineeSil/', views.CertificateRecommendByExamineeSil.as_view()),

    # CertificateRecommand By Interest & Random - 필기 - snchoi
    path('api/certificate/CertRecomByInterest/', views.CertificateRecommendByInterest),

    # CertificateRecommand By Interest & Random - 실기 - snchoi
    path('api/certificate/CertRecomByInterestSil/', views.CertificateRecommendByInterestSil),
]
