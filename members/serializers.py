from rest_framework import serializers
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
        fields = '__all__'


class WorkProfileSerializer(ModelSerializer):
    class Meta:
        model = WorkProfile
        fields = '__all__'


class PersonalProfileListSerializer(ModelSerializer):
    class Meta:
        model = PersonalProfile
        fields = ['id', 'name', 'image', 'graduation']

    image = serializers.CharField(source='avatar')


class PersonalProfileListSerializer(ModelSerializer):
    # work_profile = WorkProfileSerializer(many=True)
    class Meta:
        model = PersonalProfile
        fields = ['id', 'name', 'avatar', 'graduation']

    # image = serializers.CharField(source='avatar')


class MyProfile(ModelSerializer):
    # work_profile = WorkProfileSerializer(many=True)
    # social_profile = SocialProfileSerializer(many=True)

    class Meta:
        model = PersonalProfile
        fields = '__all__'

