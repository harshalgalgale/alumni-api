# Generated by Django 3.2.5 on 2021-07-09 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='personalprofile',
            options={'ordering': ['student'], 'verbose_name': 'Member profile', 'verbose_name_plural': 'Member profiles'},
        ),
    ]
