from rest_framework import routers

from article.views import BulletinViewSet, AlbumViewSet

router = routers.DefaultRouter()
router.register('bulletin', BulletinViewSet)
router.register('album', AlbumViewSet)

urlpatterns = []

urlpatterns += router.urls
