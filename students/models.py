from datetime import datetime

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

# Create your models here.
GENDER = [
    ('M', 'Male'),
    ('F', 'Female'),
]
DEGREE = [
    ('btech', 'B.Tech'),
    ('mtech', 'M.Tech'),
    ('phd', 'PhD'),
]
DEPARTMENT = [
    ('ape', 'APE'),
    ('fmp', 'FMP'),
    ('ide', 'IDE'),
    ('swce', 'SWCE'),
]
YEAR_CHOICES = [(r, r) for r in range(1969, datetime.today().year + 1)]
MIN_YEAR = 1900


def get_default_reg_no():
    count = Student.objects.all().count()
    return f'DRNo_{count}'


class Student(models.Model):
    reg_no = models.CharField(help_text='Student id', max_length=20, default=get_default_reg_no)
    birth_date = models.DateField(null=True, blank=True)
    first_name = models.CharField(help_text='First name', max_length=150)
    middle_name = models.CharField(help_text='Middle name', max_length=150, null=True, blank=True)
    last_name = models.CharField(help_text='Last name', max_length=150)
    degree = models.CharField(help_text='Passing degree', choices=DEGREE, max_length=10)
    department = models.CharField(help_text='Department', choices=DEPARTMENT, max_length=10, null=True, blank=True)
    reg_year = models.IntegerField(help_text='Registration year',
                                   validators=[MinValueValidator(MIN_YEAR), MaxValueValidator(datetime.now().year)],
                                   default=datetime.now().year)
    pass_year = models.IntegerField(help_text='Graduation year',
                                   validators=[MinValueValidator(MIN_YEAR), MaxValueValidator(datetime.now().year)],
                                   default=datetime.now().year)
    gender = models.CharField(choices=GENDER, max_length=1, null=True, blank=True)

    class Meta:
        verbose_name = 'Registered Student'
        verbose_name_plural = 'Registered Students'
        ordering = ['reg_no', 'last_name', 'first_name', 'middle_name', 'birth_date']
        unique_together = ['reg_no', 'degree', 'reg_year']

    def __str__(self):
        return f'{self.reg_no} : {self.get_short_name()} : {self.degree} : {self.reg_year}'

    def get_full_name(self):
        full_name = f'{self.first_name} {self.middle_name} {self.last_name}'
        return full_name.strip()

    def get_short_name(self):
        return f'{self.first_name} {self.last_name}'
