# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_babysitterprofile_parentprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='babysitterprofile',
            name='long_bio',
            field=models.TextField(null=True, verbose_name='Bakici Detay Bilgi', blank=True),
        ),
        migrations.AddField(
            model_name='parentprofile',
            name='long_bio',
            field=models.TextField(null=True, verbose_name='Ebeveyn Detay Bilgi', blank=True),
        ),
    ]
