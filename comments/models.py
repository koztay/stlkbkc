# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.conf import settings

class CommentQuerySet(models.query.QuerySet):
	def get_commented_user(self, commented_user):
		return self.filter(commented_user=commented_user)


# Create your models here.
class CommentManager(models.Manager):
	def create_comment(self, user=None, commented_user=None, comment=None):
		if not user:
			raise ValueError("Comment eklenirken ekleyen kullanıcı boş bırakılamaz.")
		if not commented_user:
			raise ValueError("Comment eklenirken ekleyen kullanıcı boş bırakılamaz.")

		comment = self.model(
			user = user,
			comment = comment,
			)

		if commented_user is not None:
			comment.commented_user = commented_user
		comment.save(using=self._db)
		return comment

	def get_queryset(self):
		return CommentQuerySet(self.model, using=self._db)

	def all_for_commented_user(self, commented_user):
		return self.get_queryset().get_commented_user(commented_user)


class Comment(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL) # this is the user instance which creates comment
	commented_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="commented_user")  # this is the user instance which will be commented
	comment_text = models.TextField()
	active = models.BooleanField(default=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	objects = CommentManager()
	# transaction_user = models.ForeignKey(settings.AUTH_USER_MODEL)
	"""
	transaction_user 'dan userlar arası transaction bilgisini almak ve transaction 
	yoksa comment ekletmemek lazım. CommentManager 'da bunu check edip ValueError verebiliriz.
	Ancak henüz transaction objem olmadığı için bunu check edemiyorum.
	Ayrıca buraya rating de eklemek lazım, ama nasıl olacak bilmiyorum. İleride ekleriz.

	"""

	def __unicode__(self):
		return self.user.name