from django.db import models

# Create your models here.
from members.models import PersonalProfile


class CommitteeMember(models.Model):
    POSITION = [
        ('00_PT', 'Patron'),
        ('01_PR', 'President'),
        ('02_VP', 'Vice President'),
        ('03_SC', 'Secretary'),
        ('04_TR', 'Treasurer'),
        ('05_MB', 'Member'),
    ]
    member = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    position = models.CharField(choices=POSITION, max_length=5)

    class Meta:
        verbose_name = 'Committee member'
        verbose_name_plural = 'Committee members'
        ordering = ['position', 'member__last_name']

    def __str__(self):
        return f'{self.member__name} : {self.position}'
