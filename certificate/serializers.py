from rest_framework import serializers
from .models import Certificate, Category, CertSchedule
from datetime import datetime

#수녕 - 테스트중
class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertSchedule.objects.select_related('cert_id').filter(test_start_date__lte=datetime.now()).order_by('test_start_date')
        fields = '__all__'

#수녕 - 테스트중     
class TestCertificateSerializer(serializers.ModelSerializer):
    # # cert_schedule model 에 있는 foreign key의 related_name을 변수로 설정
    # cert_schedule = CertScheduleSerializer(many=True, read_only=True)
    class Meta:
        model = CertSchedule
        fields = '__all__'


class CertScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertSchedule
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    # cert_schedule model 에 있는 foreign key의 related_name을 변수로 설정
    cert_schedule = CertScheduleSerializer(many=True, read_only=True)
    class Meta:
        model = Certificate
        fields = ('cert_id', 'name', 'department', 'pass_percent', 'cost', 'examinee', 'cat_id_id', 'cert_schedule')


class CategorySerializer(serializers.ModelSerializer):
    # certificate model 있는 foreign key의 related_name을 변수로 설정
    certificates = CertificateSerializer(many=True, read_only=True) 
    class Meta:
        model = Category
        fields = ('cat_id', 'name', 'certificates')

