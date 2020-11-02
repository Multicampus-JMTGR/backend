from api.models import Certificate
from .serializers import CertificateSerializer

from rest_framework import viewsets, permissions

# Certificate Viewset
class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CertificateSerializer