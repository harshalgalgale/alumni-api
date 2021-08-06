from rest_framework import routers

from core.views import MainSectorViewSet, SubSectorViewSet, SkillsViewSet

router = routers.DefaultRouter()
router.register('main-sector', MainSectorViewSet)
router.register('sub-sector', SubSectorViewSet)
router.register('skills', SkillsViewSet)

urlpatterns = []

urlpatterns += router.urls
