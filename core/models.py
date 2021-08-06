# Create your models here.
from __future__ import unicode_literals

import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username='deleted')[0]


class UUIDModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class AuditTrail(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), related_name='audit_trail_created')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(User, on_delete=models.SET(get_sentinel_user), related_name='audit_trail_updated')
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Skills(UUIDModel):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class MainSector(UUIDModel):
    name = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class SubSector(UUIDModel):
    main_sector = models.ForeignKey(MainSector, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    class Meta:
        ordering = ['name']
        unique_together = [('main_sector', 'name')]

    def __str__(self):
        return f'{self.main_sector} : {self.name}'


class AbstractAddress(models.Model):
    country = models.CharField(
        max_length=150,
        blank=True,
        default='',
        help_text="Country"
    )
    state = models.CharField(
        max_length=150,
        blank=True,
        default='',
        help_text="Region/State"
    )
    district = models.CharField(
        max_length=150,
        blank=True,
        default='',
        help_text="District"
    )
    town_city = models.CharField(
        max_length=150,
        blank=True,
        default='',
        help_text="Village/Taluka/Town/City."
    )
    street_name = models.CharField(
        max_length=255,
        blank=True,
        default='',
        help_text="Street name"
    )
    address_line = models.CharField(
        max_length=255,
        blank=True,
        help_text="House name/number"
    )
    post_code = models.CharField(
        max_length=15,
        blank=True,
        default='',
        help_text="Post/ZIP code"
    )
    plus_code = models.CharField(
        max_length=20,
        blank=True,
        default='',
        help_text="Plus code (https://maps.google.com/pluscodes/)"
    )

    class Meta:
        abstract = True

    @property
    def address(self):
        return dict(
            property_name_number=self.address_line,
            street_name=self.street_name,
            town_city=self.town_city,
            district=self.district,
            state=self.state,
            country=self.country,
            post_code=self.post_code,
            plus_code=self.plus_code
        )
