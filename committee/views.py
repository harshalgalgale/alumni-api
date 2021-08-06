from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from committee.models import CommitteeMember
from committee.serializers import CommitteeMemberSerializer


class CommitteeMemberViewSet(ModelViewSet):
    queryset = CommitteeMember.objects.all()
    serializer_class = CommitteeMemberSerializer
    permission_classes = (AllowAny,)
