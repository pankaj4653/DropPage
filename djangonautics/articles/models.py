# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User



class Article(models.Model):
	author=models.ForeignKey(User,on_delete=models.CASCADE,default=None)
	title = models.CharField(max_length=100)
	slug = models.SlugField()
	body = models.TextField()
	date = models.DateTimeField(auto_now_add = True)
	thumb = models.ImageField(default="default.png",blank=True)



	def __str__(self):
		return self.title

	def snippet(self):
		return self.body[:50]+"..."


# Create your models here.