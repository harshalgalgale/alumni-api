from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from core.models import MainSector, SubSector, Skills
from core.serializers import MainSectorSerializer, SubSectorSerializer, SkillsSerializer


class MainSectorViewSet(ModelViewSet):
    queryset = MainSector.objects.all()
    serializer_class = MainSectorSerializer
    permission_classes = (AllowAny,)


class SubSectorViewSet(ModelViewSet):
    queryset = SubSector.objects.all()
    serializer_class = SubSectorSerializer
    permission_classes = (AllowAny,)


class SkillsViewSet(ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer
    permission_classes = (AllowAny,)


