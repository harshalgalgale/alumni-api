from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from members.models import PersonalProfile, WorkProfile, SocialProfile, PermanentAddress, ProfessionalSkills
from members.serializers import PersonalProfileSerializer, MyProfile, PersonalProfileListSerializer


class PersonalProfileViewSet(ModelViewSet):
    queryset = PersonalProfile.objects.all()
    serializer_class = PersonalProfileSerializer
    permission_classes = (AllowAny,)


class MembersListView(APIView):

    def get(self, request, format=None):
        queryset = PersonalProfile.objects.all()
        # serializer = PersonalProfileSerializer(queryset, many=True)
        serializer = PersonalProfileListSerializer(queryset, many=True)
        return Response(serializer.data)


def get_profile_details(user_profile):
    user_address = PermanentAddress.objects.filter(personal_profile=user_profile)
    if user_address:
        user_address_dict = user_address.last().address
    else:
        user_address_dict = {}
    work_profiles = WorkProfile.objects.filter(personal_profile=user_profile)
    if work_profiles:
        work_profile = work_profiles.last()
        work_profile_dict = dict(
            sector={'id': work_profile.sector.id, 'name': work_profile.sector.name},
            organisation=work_profile.organisation,
            position=work_profile.position,
            role=work_profile.role,
            url=work_profile.url,
            address=work_profile.address
        )
    else:
        work_profile_dict = {}
    social_profile = SocialProfile.objects.filter(personal_profile=user_profile,
                                                  social_media='linkedin').last()
    skills = ProfessionalSkills.objects.filter(personal_profile=user_profile)
    if social_profile:
        social_profile_url = social_profile.url
    else:
        social_profile_url = None
    if user_profile.avatar:
        user_image = user_profile.avatar.url
    else:
        user_image = None
    status_code = status.HTTP_200_OK
    response = {
        'success': 'true',
        'status code': status_code,
        'message': 'User profile fetched successfully',
        'data': {
            'id': user_profile.id,
            'name': user_profile.name,
            'personal_profile': {
                'first_name': user_profile.first_name,
                'middle_name': user_profile.middle_name,
                'last_name': user_profile.last_name,
                'birth_date': user_profile.birth_date.isoformat(),
                'phone': user_profile.phone,
                'email': user_profile.user.email,
                'gender': user_profile.gender,
                'avatar': user_image,
                'bio': user_profile.bio,
                'address': user_address_dict
            },
            'work_profile': work_profile_dict,
            'linkedin': social_profile_url,
            'skills': [
                {'id': skill.id, 'name': skill.name} for skill in skills
            ],
            'blogs': []
        },
    }
    return response, status_code


class MembersDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PersonalProfile.objects.get(id=pk)
        except PersonalProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_profile = self.get_object(pk)
        response, status_code = get_profile_details(user_profile)
        return Response(response, status=status_code)

    def put(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = PersonalProfileSerializer(member, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        member = self.get_object(pk)
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserProfileView(RetrieveAPIView):

    permission_classes = (IsAuthenticated,)
    # authentication_class = JSONWebTokenAuthentication

    def get(self, request):
        user_profile = PersonalProfile.objects.get(user=request.user)
        response, status_code = get_profile_details(user_profile)
        return Response(response, status=status_code)


class MembersSearchView(generics.ListAPIView):
    queryset = PersonalProfile.objects.all().select_related('student')
    serializer_class = PersonalProfileListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']


class MembersSummaryView(generics.ListAPIView):

    def get(self, request):
        queryset = PersonalProfile.objects.all().select_related('student')
        total = queryset.count()
        graduates = queryset.filter(student__degree='btech').count()
        post_graduates = queryset.filter(student__degree='mtech').count()
        phds = queryset.filter(student__degree='phd').count()
        status_code = status.HTTP_200_OK
        response = {
            'success': 'true',
            'status code': status_code,
            'message': 'Summary fetched successfully',
            'data': [
                {'id': 1, 'title': 'Members', 'count': total, 'image': 'assets/images/illustrator/Asset190.svg'},
                {'id': 2, 'title': 'Graduates', 'count': graduates, 'image': 'assets/images/illustrator/Asset189.svg'},
                {'id': 3, 'title': 'Post Graduates', 'count': post_graduates, 'image': 'assets/images/illustrator/Asset192.svg'},
                {'id': 4, 'title': 'PhDs', 'count': phds, 'image': 'assets/images/illustrator/Asset187.svg'},
            ]
        }
        return Response(response, status=status_code)
