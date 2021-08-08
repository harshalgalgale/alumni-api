from django.conf.urls import url
from rest_framework import routers

from students.views import StudentViewSet, BatchUploadStudentsView

router = routers.DefaultRouter()
router.register('', StudentViewSet)

urlpatterns = [
    url(r'^upload/students/', BatchUploadStudentsView.as_view(),
        name='batch_upload_students'),

]

urlpatterns += router.urls
