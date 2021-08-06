from django.db import models
from django.contrib.auth import get_user_model

from core.models import AbstractAddress
from members.models import PersonalProfile
from students.models import DEGREE

User = get_user_model()
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo =models.FileField(blank=True, null=True)
    url = models.URLField(help_text='Company URL', blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class CompanyAddress(AbstractAddress):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    class Meta:
        ordering = ['company__name', 'country']

    def __str__(self):
        return f'{self.company.name} : {self.country} : {self.state}'


class JobAdvert(models.Model):
    EMPLOYMENT_TYPE = [
        ('permanent', 'Permanent'),
        ('parttime', 'Part-time'),
        ('contract', 'Contract'),
    ]
    company_location = models.ForeignKey(CompanyAddress, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    url = models.URLField(help_text='Job URL', blank=True)
    min_experience = models.IntegerField(help_text='Experience in years', default=0)
    min_qualification = models.CharField(choices=DEGREE, max_length=10)
    min_salary = models.IntegerField(default=0)
    max_salary = models.IntegerField(default=0)
    employment_type = models.CharField(choices=EMPLOYMENT_TYPE, max_length=10)
    last_date = models.DateField()
    owner = models.ForeignKey(PersonalProfile, on_delete=models.CASCADE)
    view_count = models.IntegerField(default=0)

    class Meta:
        ordering = ['-last_date']

    def __str__(self):
        return f'{self.title} : {self.company_location.company.name}'
