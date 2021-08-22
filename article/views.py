from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import ModelViewSet

from article.models import Bulletin, Album
from article.serializers import BulletinSerializer, AlbumSerializer


class SimplePagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    page_query_param = 'page'
    page_size = 20
    max_page_size = 1000


class BulletinViewSet(ModelViewSet):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (IsAuthenticated,)


class AlbumViewSet(ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsAuthenticated,)


class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (AllowAny,)


class BulletinList(generics.ListCreateAPIView):
    queryset = Bulletin.objects.all()
    serializer_class = BulletinSerializer
    permission_classes = (AllowAny,)


class LatestBulletinList(generics.ListCreateAPIView):
    queryset = Bulletin.objects.all()
    paginator = SimplePagination()
    serializer_class = BulletinSerializer
    permission_classes = (AllowAny,)
