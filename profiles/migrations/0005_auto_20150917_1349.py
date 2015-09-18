# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20150917_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='babysitterprofile',
            name='ikametgah',
            field=models.FileField(upload_to=profiles.models.get_upload_path, null=True, verbose_name='\u0130kametgah', blank=True),
        ),
        migrations.AddField(
            model_name='babysitterprofile',
            name='ogrenci_belgesi',
            field=models.FileField(upload_to=profiles.models.get_upload_path, null=True, verbose_name='\xd6\u011frenci Belgesi', blank=True),
        ),
        migrations.AddField(
            model_name='babysitterprofile',
            name='sabika_kaydi',
            field=models.FileField(upload_to=profiles.models.get_upload_path, null=True, verbose_name='Sab\u0131ka Kayd\u0131', blank=True),
        ),
    ]
