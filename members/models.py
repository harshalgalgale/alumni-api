from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from core.models import AbstractAddress, SubSector, Skills
from students.models import Student, GENDER
User = get_user_model()


class PersonalProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255)
    birth_date = models.DateField(null=True, blank=True)
    phone = models.CharField(max_length=30, null=True, blank=True)
    gender = models.CharField(choices=GENDER, max_length=1, null=True, blank=True)
    avatar = models.FileField(null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = 'Member profile'
        verbose_name_plural = 'Member profiles'
        ordering = ['student']

    def __str__(self):
        return f'{self.user.name}'

    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'


class WorkProfile(AbstractAddress):
    personal_profile = models.OneToOneField(PersonalProfile, on_delete=models.CASCADE)
    sector = models.OneToOneField(SubSector, on_delete=models.SET_NULL, null=True)
    organisation = models.CharField(help_text='Organisation name', max_length=150, blank=True)
    position = models.CharField(help_text='Position title', max_length=150, blank=True)
    role = models.CharField(help_text='Role description', max_length=150, blank=True)
    url = models.URLField(help_text='Organisation url', max_length=150, blank=True)

    class Meta:
        ordering = ['personal_profile']

    def __str__(self):
        return f'{self.personal_profile} : {self.organisation} : {self.sector}'


class PermanentAddress(AbstractAddress):
    personal_profile = models.OneToOneField(PersonalProfile, on_delete=models.CASCADE)

    class Meta:
        ordering = ['personal_profile']

    def __str__(self):
        return f'{self.personal_profile} : {self.country} : {self.state}'


class SocialProfile(models.Model):
    SOCIAL = [
        ('linkedin', 'LinkedIn'),
        ('facebook', 'Facebook'),
        ('instagram', 'Instagram'),
    ]
    personal_profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    social_media = models.CharField(help_text='Social channel', choices=SOCIAL, max_length=10)
    url = models.URLField(help_text='Social handle', blank=True)

    class Meta:
        ordering = ['personal_profile']
        unique_together = [('personal_profile', 'social_media')]

    def __str__(self):
        return f'{self.personal_profile} : {self.social_media}'


class ProfessionalSkills(models.Model):
    personal_profile = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skills, on_delete=models.CASCADE)

    class Meta:
        ordering = ['personal_profile']
        unique_together = [('personal_profile', 'skill')]
