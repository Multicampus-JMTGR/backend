from rest_framework import serializers
from .models import Certificate, Category, CertSchedule

class CertScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertSchedule
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    schedule = CertScheduleSerializer(many=True, read_only=True)
    class Meta:
        model = Certificate
        fields = ('cert_id', 'name', 'department', 'pass_percent', 'cost', 'examinee', 'cat_id_id', 'schedule')

class CategorySerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('cat_id', 'name', 'certificates')

