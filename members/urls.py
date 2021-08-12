from django.urls import path
from rest_framework import routers

from members.views import PersonalProfileViewSet, MembersListView, MembersDetailView, UserProfileView, MembersSearchView

router = routers.DefaultRouter()
# router.register('profile', PersonalProfileViewSet)


urlpatterns = [
    # path('', MembersListView.as_view(), name='members-list'),
    path('', MembersSearchView.as_view(), name='members-list'),
    path('profile/me/', UserProfileView.as_view(), name='profile-me'),
    path('<int:pk>/', MembersDetailView.as_view(), name='members-detail')
]

urlpatterns += router.urls
