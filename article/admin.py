from django.contrib import admin

# Register your models here.
from article.models import Bulletin, Album, AlbumImage


@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    pass


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(AlbumImage)
class AlbumImageAdmin(admin.ModelAdmin):
    pass
