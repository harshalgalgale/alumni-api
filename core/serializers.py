from rest_framework.serializers import ModelSerializer

from core.models import MainSector, SubSector, Skills


class MainSectorSerializer(ModelSerializer):
    class Meta:
        model = MainSector
        fields = '__all__'


class SubSectorSerializer(ModelSerializer):
    class Meta:
        model = SubSector
        fields = '__all__'


class SkillsSerializer(ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'
