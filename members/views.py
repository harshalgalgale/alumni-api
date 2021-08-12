from django.http import Http404
from rest_framework import status, generics, filters
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from members.models import PersonalProfile, WorkProfile, SocialProfile, PermanentAddress
from members.serializers import PersonalProfileSerializer, MyProfile


class PersonalProfileViewSet(ModelViewSet):
    queryset = PersonalProfile.objects.all()
    serializer_class = PersonalProfileSerializer
    permission_classes = (AllowAny,)


class MembersListView(APIView):

    def get(self, request, format=None):
        queryset = PersonalProfile.objects.all()
        serializer = PersonalProfileSerializer(queryset, many=True)
        return Response(serializer.data)


class MembersDetailView(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return PersonalProfile.objects.get(pk=pk)
        except PersonalProfile.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        member = self.get_object(pk)
        serializer = PersonalProfileSerializer(member)
        return Response(serializer.data)

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
        try:
            user_profile = PersonalProfile.objects.get(user=request.user)
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
                    # address=dict(
                    #     property_name_number=work_profile.address_line,
                    #     street_name=work_profile.street_name,
                    #     town_city=work_profile.town_city,
                    #     district=work_profile.district,
                    #     state=work_profile.state,
                    #     country=work_profile.country,
                    #     post_code=work_profile.post_code,
                    #     plus_code=work_profile.plus_code
                    # )
                )
            else:
                work_profile_dict = {}
            print(work_profile_dict)
            social_profile = SocialProfile.objects.filter(personal_profile=user_profile, social_media='linkedin').last()
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
                        'avatar': user_profile.avatar.url,
                        'bio': user_profile.bio,
                        'address': user_address_dict
                    },
                    'work_profile': work_profile_dict,
                    'linkedin': social_profile.url,
                    'skills': [
                        {'id': 1, 'name': 'Software Development'},
                        {'id': 2, 'name': 'Team Management'},
                        {'id': 3, 'name': 'GIS'},
                        {'id': 4, 'name': 'Remote Sensing'}
                    ],
                    'blogs': []
                    },
                }
            print(response)

        except Exception as e:
            status_code = status.HTTP_400_BAD_REQUEST
            response = {
                'success': 'false',
                'status code': status.HTTP_400_BAD_REQUEST,
                'message': 'User does not exists',
                'error': str(e)
                }
        return Response(response, status=status_code)


class MembersSearchView(generics.ListAPIView):
    queryset = PersonalProfile.objects.all()
    serializer_class = PersonalProfileSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']
