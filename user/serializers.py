from rest_framework import serializers
from .models import User
from certificate.models import Certificate, Category, StudyPlan
from certificate.serializers import CertificateSerializer, CategorySerializer, StudyPlanSerializer


class UserSerializer(serializers.ModelSerializer):
    liked_certs = CertificateSerializer(many=True, read_only=True)
    liked_cats = CategorySerializer(many=True, read_only=True)
    study_plan = StudyPlanSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = '__all__'