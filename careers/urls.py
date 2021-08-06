from rest_framework import routers

from careers.views import CompanyViewSet, JobAdvertViewSet, CompanyAddressViewSet

router = routers.DefaultRouter()
router.register('company', CompanyViewSet)
router.register('company-address', CompanyAddressViewSet)
router.register('jobs', JobAdvertViewSet)


urlpatterns = []

urlpatterns += router.urls
