from django.contrib import admin

# Register your models here.
from article.models import Bulletin, Album, AlbumImage


@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']
    save_as = True


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    raw_id_fields = ['author']
    save_as = True


@admin.register(AlbumImage)
class AlbumImageAdmin(admin.ModelAdmin):
    pass
