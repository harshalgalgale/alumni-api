from rest_framework import routers

from students.views import StudentViewSet

router = routers.DefaultRouter()
router.register('', StudentViewSet)

urlpatterns = []

urlpatterns += router.urls
