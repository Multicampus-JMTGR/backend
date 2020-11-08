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

    # Certificate Ordering Filter - minji
    path('certificate/OrderingFilter/', views.CertificateOrderingFilter.as_view()), #테스트중

    # CertificateRecommand By Pilgi Examinee - snchoi
    path('certificate/CertRecomByExaminee/', views.CertificateRecommendByExaminee.as_view()),

    # CertificateRecommand By Silgi Examinee - snchoi
    path('certificate/CertRecomByExamineeSil/', views.CertificateRecommendByExamineeSil.as_view()), #테스트중

    # CertificateRecommand By Interest(회원) - snchoi
    path('certificate/CertRecomByInterest/', views.CertificateRecommendByInterest), #테스트중

    # CertificateRecommand By Random(비회원) - snchoi
    path('certificate/CertRecomByRandom/', views.CertificateRecommendByRandom), #테스트중
]
