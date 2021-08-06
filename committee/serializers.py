from rest_framework.serializers import ModelSerializer

from committee.models import CommitteeMember


class CommitteeMemberSerializer(ModelSerializer):
    class Meta:
        model = CommitteeMember
        fields = '__all__'
