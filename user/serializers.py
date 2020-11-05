from rest_framework import serializers
from .models import User, StudyPlan
from certificate.models import Certificate, Category
from certificate.serializers import CertificateSerializer, CategorySerializer

class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    liked_certs = CertificateSerializer(many=True, read_only=True)
    liked_cats = CategorySerializer(many=True, read_only=True)
    study_plan = StudyPlanSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'
