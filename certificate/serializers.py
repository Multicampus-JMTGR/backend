from rest_framework import serializers
from api.models import Certificate, User

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'