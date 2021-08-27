from django.conf.urls import url
from django.urls import path
from rest_framework import routers

from members.views import PersonalProfileViewSet, MembersListView, MembersDetailView, UserProfileView, \
    MembersSearchView, MembersSummaryView, WorkProfileViewSet, SocialProfileViewSet, PermanentAddressViewSet, \
    ProfessionalSkillsViewset

# , update_work, update_social, update_personal, update_address

router = routers.DefaultRouter()
router.register('profile', PersonalProfileViewSet)
router.register('profile-work', WorkProfileViewSet)
router.register('profile-social', SocialProfileViewSet)
router.register('profile-skills', ProfessionalSkillsViewset)
router.register('profile-address', PermanentAddressViewSet)


urlpatterns = [
    # path('', MembersListView.as_view(), name='members-list'),
    # url(r'update_work_profile/', update_work),
    # url(r'update_social_profile/', update_social),
    # url(r'update_personal_profile/', update_personal),
    # url(r'update_address_profile/', update_address),
    path('', MembersSearchView.as_view(), name='members-list'),
    path('summary/', MembersSummaryView.as_view(), name='members-summary'),
    path('profile/me/', UserProfileView.as_view(), name='profile-me'),
    path('<int:pk>/', MembersDetailView.as_view(), name='members-detail')
]

urlpatterns += router.urls
