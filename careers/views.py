from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from careers.models import Company, JobAdvert
from careers.serializers import CompanySerializer, JobAdvertSerializer, CompanyAddressSerializer


class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = (AllowAny,)


class CompanyAddressViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyAddressSerializer
    permission_classes = (AllowAny,)


class JobAdvertViewSet(ModelViewSet):
    queryset = JobAdvert.objects.all()
    serializer_class = JobAdvertSerializer
    permission_classes = (AllowAny,)


