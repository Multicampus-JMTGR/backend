from rest_framework import serializers
from .models import Certificate, Category, StudyPlan

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ('cert_id', 'name', 'department', 'pass_percent', 'cost', 'cat_id_id')

class CategorySerializer(serializers.ModelSerializer):
    certificates = CertificateSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ('cat_id', 'name', 'certificates')

