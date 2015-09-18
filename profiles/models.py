# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    picture = models.ImageField('Profil resmi',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    #bio = models.CharField("Kısa Biypgrafi", max_length=200, blank=True, null=True) Bu alana gerek yok. iüiğçö
    email_verified = models.BooleanField("Email onayı", default=False)

    class Meta:
        abstract = True


def get_upload_path(instance, filename):
    name, ext = filename.split('.')
    file_path = 'bakici-belgeleri/{username}/{name}.{ext}'.format(
        username=instance.user.name , name=name, ext=ext) 
    return file_path

@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)


@python_2_unicode_compatible
class ParentProfile(BaseProfile):
    profile_type = "Profile type is ParentProfile"

    long_bio = models.TextField("Ebeveyn Detay Bilgi", blank=True, null=True)

    def __str__(self):
        return "{}'s profile". format(self.user)


@python_2_unicode_compatible
class BabySitterProfile(BaseProfile):
    profile_type = "Profile type is BabySitterProfile"

    long_bio = models.TextField("Bakıcı Detay Bilgi", blank=True, null=True)

    ikametgah = models.FileField('İkametgah',
                                upload_to=get_upload_path,
                                null=True,
                                blank=True)
    sabika_kaydi = models.FileField('Sabıka Kaydı',
                                upload_to=get_upload_path,
                                null=True,
                                blank=True)

    ogrenci_belgesi = models.FileField('Öğrenci Belgesi',
                                upload_to=get_upload_path,
                                null=True,
                                blank=True)

    def __str__(self):
        return "{}'s profile". format(self.user)
