from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from article.models import Bulletin, Album
from article.serializers import BulletinSerializer, AlbumSerializer


class BulletinViewSet(ModelViewSet):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (IsAuthenticated,)



class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)
