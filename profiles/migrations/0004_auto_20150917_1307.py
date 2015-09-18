# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_auto_20150914_2021'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='babysitterprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='parentprofile',
            name='bio',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='bio',
        ),
        migrations.AlterField(
            model_name='babysitterprofile',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email onay\u0131'),
        ),
        migrations.AlterField(
            model_name='babysitterprofile',
            name='long_bio',
            field=models.TextField(null=True, verbose_name='Bak\u0131c\u0131 Detay Bilgi', blank=True),
        ),
        migrations.AlterField(
            model_name='babysitterprofile',
            name='picture',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Profil resmi', blank=True),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email onay\u0131'),
        ),
        migrations.AlterField(
            model_name='parentprofile',
            name='picture',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Profil resmi', blank=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email_verified',
            field=models.BooleanField(default=False, verbose_name='Email onay\u0131'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(upload_to='profile_pics/%Y-%m-%d/', null=True, verbose_name='Profil resmi', blank=True),
        ),
    ]
