from rest_framework import serializers
from .models import Certificate, Category, CertSchedule

class CertScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertSchedule
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    # cert_schedule model 에 있는 foreign key의 related_name을 변수로 설정
    cert_schedule = CertScheduleSerializer(many=True, read_only=True) 
    class Meta:
        model = Certificate
        fields = ('cert_id', 'name', 'department', 'pass_percent', 'cost', 'examinee', 'cat_id_id', 'schedule')


class CategorySerializer(serializers.ModelSerializer):
    # certificate model 있는 foreign key의 related_name을 변수로 설정
    certificates = CertificateSerializer(many=True, read_only=True) 
    class Meta:
        model = Category
        fields = ('cat_id', 'name', 'certificates')

