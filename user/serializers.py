from rest_framework import serializers
from .models import User, StudyPlan
from certificate.models import Certificate, Category
from certificate.serializers import CertificateSerializer, CategorySerializer, CertScheduleSerializer

class StudyPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyPlan
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    cert_likes = CertificateSerializer(many=True, read_only=True)
    cat_likes = CategorySerializer(many=True, read_only=True)
    cert_schedule = CertScheduleSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ('email', 'interest', 'name', 'phone_number', 'cat_likes', 'cert_likes', 'cert_schedule')


    def update(self, request, instance, validated_data, cert_id):
        instance.email = validated_data.get('email', instance.email)
        instance.interest = validated_data.get('interest', instance.interest)
        instance.name = validated_data.get('name', instance.name)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.cat_id = validated_data.get('cat_id', instance.cat_id)
        like_exists = validated_data.filter('cert_likes', cert_id)

        if like_exists == "":
            instance.cert_likes.add(cert_id)
        else:
            instance.cert_likes.remove(cert_id)
        
        instance.save()