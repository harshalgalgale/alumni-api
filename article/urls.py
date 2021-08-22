from django.urls import path
from rest_framework import routers

from article.views import BulletinViewSet, AlbumViewSet, AlbumList, BulletinList, LatestBulletinList

router = routers.DefaultRouter()
router.register('bulletin', BulletinViewSet)
router.register('album', AlbumViewSet)

urlpatterns = [
    path('gallery/', AlbumList.as_view(), name='gallery-list'),
    path('ebulletin/', BulletinList.as_view(), name='bulletin-list'),
    path('latest-bulletin/', LatestBulletinList.as_view(), name='latest-bulletin'),
]

urlpatterns += router.urls
