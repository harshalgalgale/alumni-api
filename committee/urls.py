from rest_framework import routers

from committee.views import CommitteeMemberViewSet

router = routers.DefaultRouter()
router.register('member', CommitteeMemberViewSet)

urlpatterns = []

urlpatterns += router.urls
