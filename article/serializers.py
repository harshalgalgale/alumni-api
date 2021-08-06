from rest_framework.serializers import ModelSerializer

from article.models import Bulletin, Album


class BulletinSerializer(ModelSerializer):
    class Meta:
        model = Bulletin
        fields = '__all__'


class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__'
        depth = 1
