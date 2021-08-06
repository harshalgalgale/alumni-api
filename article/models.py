from django.db import models

# Create your models here.
from members.models import PersonalProfile


class AbstractArticle(models.Model):
    feature_image = models.FileField(blank=False, null=False)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    pub_date = models.DateField()
    view_count = models.IntegerField(default=0)
    clap_count = models.IntegerField(default=0)

    class Meta:
        abstract = True


class Bulletin(AbstractArticle):
    file = models.FileField(blank=False, null=False)

    class Meta:
        verbose_name = 'Bulletin'
        verbose_name_plural = 'Bulletins'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title} : {self.author}'


class Album(AbstractArticle):

    class Meta:
        verbose_name = 'Album'
        verbose_name_plural = 'Albums'
        ordering = ['-pub_date']

    def __str__(self):
        return f'{self.title} : {self.author}'


class AlbumImage(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name="Image", blank=True, null=True, upload_to='album')

    def __str__(self):
        return f'{self.album} : {self.image}'
