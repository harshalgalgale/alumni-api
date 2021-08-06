from rest_framework.serializers import ModelSerializer

from members.models import PersonalProfile, SocialProfile, WorkProfile


class PersonalProfileSerializer(ModelSerializer):
    class Meta:
        model = PersonalProfile
        fields = '__all__'
        depth = 0


class SocialProfileSerializer(ModelSerializer):
    class Meta:
        model = SocialProfile


class WorkProfileSerializer(ModelSerializer):
    class Meta:
        model = WorkProfile


class MyProfile(ModelSerializer):
    # work_profile = WorkProfileSerializer(many=True)
    # social_profile = SocialProfileSerializer(many=True)

    class Meta:
        model = PersonalProfile
        fields = '__all__'

