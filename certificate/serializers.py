from rest_framework import serializers
from .models import Certificate, Category, CertSchedule
from datetime import datetime

# CertificateSchedule + Certificate.name
class CertNameCertScheduleSerializer(serializers.ModelSerializer):
    certificates_name = serializers.CharField(read_only=True, source="cert_id.name")
    class Meta:
        model = CertSchedule
        fields = ('cert_id', 'test_type', 'test_round', 'reg_start_date', 'reg_end_date', 'test_start_date', 'test_end_date', 'result_date_1', 'result_date_2', 'certificates_name',)


# Category 기본정보
class PureCategoryNameOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')

# Category 기본정보
class PureCategoryOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# Certificate 기본정보
class CertificateOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'


# CertSchedule 기본정보
class CertScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertSchedule
        fields = '__all__'


# Category + Certificate
class CatCertSerializer(serializers.ModelSerializer):
    certificates = CertificateOnlySerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('cat_id', 'name', 'certificates')


# Certificate + CertSchedule
class CertificateSerializer(serializers.ModelSerializer):
    # cert_schedule model 에 있는 foreign key의 related_name을 변수로 설정
    cert_schedule = CertScheduleSerializer(many=True, read_only=True)
    class Meta:
        model = Certificate
        fields = ('cert_id', 'name', 'department', 'pass_percent', 'pass_percent_sil', 'cost', 'cost_sil',\
                  'examinee', 'examinee_sil', 'cat_id_id', 'cert_schedule')


# Category + Certificate + CertSchedule
class CategorySerializer(serializers.ModelSerializer):
    # certificate model 있는 foreign key의 related_name을 변수로 설정
    certificates = CertificateSerializer(many=True, read_only=True) 
    class Meta:
        model = Category
        fields = ('cat_id', 'name', 'certificates')


