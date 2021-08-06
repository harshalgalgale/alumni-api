from rest_framework.serializers import ModelSerializer

from careers.models import Company, JobAdvert, CompanyAddress


class CompanySerializer(ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CompanyAddressSerializer(ModelSerializer):
    class Meta:
        model = CompanyAddress
        fields = '__all__'


class JobAdvertSerializer(ModelSerializer):
    class Meta:
        model = JobAdvert
        fields = '__all__'

