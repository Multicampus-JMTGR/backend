from django.urls import path, include
from .views import HelloAPI
from . import views

urlpatterns = [

    # Certificate Schedule
    path('certschedule/', views.ListCertSchedule.as_view()),
    path('certschedule/<int:pk>', views.DetailCertSchedule.as_view()),
    
    # Certificates
    path('certificate/', views.ListCertificates.as_view()),
    path('certificate/<int:pk>', views.DetailCertificates.as_view()),

     # Category
    path('category/', views.ListCategories.as_view()),
    path('category/<int:pk>', views.DetailCategories.as_view()),
    
    # Certificates Filter - snchoi
    path('certificate/CertificatesFilter/', views.CertifiacetFilterSearchAPI),

    # Certificate Ordering Filter - snchoi
    path('certificate/OrderingFilter/', views.CertificateOrderingFilter.as_view()), #테스트중

    # CertificateRecommand By 필기 Examinee - snchoi
    path('certificate/CertRecomByExaminee/', views.CertificateRecommendByExaminee.as_view()),

    # CertificateRecommand By 실기 Examinee - snchoi
    path('certificate/CertRecomByExamineeSil/', views.CertificateRecommendByExamineeSil.as_view()),

    # CertificateRecommand By Interest & Random - 필기 - snchoi
    path('certificate/CertRecomByInterest/', views.CertificateRecommendByInterest),

    # CertificateRecommand By Interest & Random - 실기 - snchoi
    path('certificate/CertRecomByInterestSil/', views.CertificateRecommendByInterestSil)
]
